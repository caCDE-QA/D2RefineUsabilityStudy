from __future__ import division

import glob
import draw
import sparql
import os
import subprocess
import workflows
from rdflib import Graph, URIRef
from rdflib.plugins.sparql import prepareQuery

PROJECTS = ["D2Refine", "OntoMaton", "RightField"]
LABELS =["Activity Model\n(In Use)", "User Model\n(Wanted)", "Designer Model\n(Implemented)"]

# Activity, Designer, User
#(100, 010, 110, 001, 101, 011, 111)
def get_venn_data(activity, designer, user):
    total_count = len(activity.union(designer).union(user))

    def to_percent(x):
        print len(x), total_count
        return str(int(round(len(x) / total_count, 2) * 100)) + '%'
    return (
        to_percent(activity.difference(designer).difference(user)), #100 activity
        to_percent(user.difference(designer).difference(activity)), #010 user
        to_percent(activity.intersection(user).difference(designer)), #110
        to_percent(designer.difference(user).difference(activity)), #001 designer
        to_percent(activity.intersection(designer).difference(user)), #101
        to_percent(designer.intersection(user).difference(activity)), #011
        to_percent(activity.intersection(designer).intersection(user)) #111
    )

def get_count(uri):
    return int(next(iter(g.query(prepareQuery(sparql.get_instance_counts), initBindings={'clazz': uri}))).cnt)

def get_uris(uri):
    return set(str(r.instance) for r in g.query(prepareQuery(sparql.get_instances), initBindings={'clazz': uri}))

os.environ["PELLET_HOME"] = "<PATH_TO_PALLET_REASONER_INSTALL_DIRECTORY>"

result = subprocess.check_output(["sh", "<PATH_TO_PALLET_REASONER_INSTALL_DIRECTORY>/pellet.sh", "extract", "-s", "AllStatements", "<PATH_TO_WORK_DOMAIN_ONTOLOGY>"])

g = Graph()
g.parse(data=result, format='xml')

functions = get_uris(URIRef('http://id.mayo.edu/vsw#Function'))
all_designer_model_functions = get_uris(URIRef('http://id.mayo.edu/vsw#DesignerModelFunction'))
all_designer_model_functions_count = len(all_designer_model_functions)

print "All Functions: %s" % len(functions)
print "All Designer Model: %s" % all_designer_model_functions_count

venn_data = []
totals = []
within_model_domain_data = []
across_model_domain_data = []

designer_model_functions = get_uris(URIRef('http://id.mayo.edu/vsw#DesignerModelFunction'))
designer_model_functions_count = len(designer_model_functions)

open('data/within-model-domain-functions-saturation.txt', 'w').close()
open('data/across-model-domain-functions-saturation.txt', 'w').close()

for project in PROJECTS:
    designer_model_functions = get_uris(URIRef('http://id.mayo.edu/vsw#%sDesignerModelFunction' % project))
    designer_model_functions_count = len(designer_model_functions)

    domain_functions = get_uris(URIRef('http://id.mayo.edu/vsw#DomainFunction'))
    domain_functions_count = len(domain_functions)

    domain_designer_model_functions_count = len(designer_model_functions.intersection(domain_functions))

    activity_model_functions = get_uris(URIRef('http://id.mayo.edu/vsw#%sActivityModelFunction' % project))
    activity_model_functions_count = len(activity_model_functions)

    user_model_functions = get_uris(URIRef('http://id.mayo.edu/vsw#UserModelFunction'))
    user_model_functions_count = len(user_model_functions)

    total_count = len(designer_model_functions.union(activity_model_functions).union(user_model_functions))

    print "(%s) Activity Model: (%i)" % (project, activity_model_functions_count)
    print "(%s) Designer Model: (%i)" % (project, designer_model_functions_count)
    print "(%s) User Model: (%i)" % (project, user_model_functions_count)
    print "(%s) Total Model: (%i)" % (project, total_count)

    with open('data/within-model-domain-functions-saturation.txt', 'a') as f:
        # % of implemented functionality considered useful to users
        # Percentage of domain functions in the Designer Model over all functions in the Designer Model
        data = (project, domain_designer_model_functions_count/designer_model_functions_count * 100, domain_designer_model_functions_count, designer_model_functions_count)

        print "(%s) Within-Model Domain Function Saturation: %i (%i/%i)" % data
        f.write("%s\t%i\n" % (data[0], data[1]))

    with open('data/across-model-domain-functions-saturation.txt', 'a') as f:
        # % of useful functionality implemented
        # Percentage of domain functions in the Designer Model over domain functions in all three models
        data = (project, designer_model_functions_count/total_count * 100, domain_designer_model_functions_count, total_count)

        print "(%s) Across-Model Domain Function Saturation: %i (%i/%i)" % data
        f.write("%s\t%i\n" % (data[0], data[1]))

    venn_data.append(get_venn_data(activity_model_functions, designer_model_functions, user_model_functions))
    totals.append(total_count)

draw.draw_example_venn()
draw.draw_venn(LABELS, venn_data, totals)