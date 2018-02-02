count_functions = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX vsw: <http://id.mayo.edu/vsw#>

SELECT (COUNT(DISTINCT ?subject) AS ?count)
WHERE { ?subject rdfs:subClassOf* vsw:Function
    OPTIONAL {
                ?x rdfs:subClassOf  ?subject .
                ?y rdfs:subClassOf  ?subject .
                FILTER (?x != ?y)
    }
    FILTER(!bound(?x))
}
'''

get_functions = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX vsw: <http://id.mayo.edu/vsw#>

SELECT ?subject
WHERE { ?subject rdfs:subClassOf* vsw:Function
    OPTIONAL {
                ?x rdfs:subClassOf  ?subject .
                ?y rdfs:subClassOf  ?subject .
                FILTER (?x != ?y)
    }
    FILTER(!bound(?x))
}
'''

get_instances = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX vsw: <http://id.mayo.edu/vsw#>

SELECT ?instance

WHERE {
  ?instance rdf:type ?function ;
            vsw:isImplemented "true"^^xsd:boolean .
}
'''

get_instances = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX vsw: <http://id.mayo.edu/vsw#>

SELECT ?instance

WHERE {
  ?instance rdf:type ?clazz  .
}
'''

get_instance_counts = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX vsw: <http://id.mayo.edu/vsw#>

SELECT (COUNT(DISTINCT ?instance) AS ?cnt)

WHERE {
  ?instance rdf:type ?clazz  .
}
'''