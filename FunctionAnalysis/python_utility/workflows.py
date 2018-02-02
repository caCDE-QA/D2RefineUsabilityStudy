def to_dat(project, workflow):
    for k in workflow:
        with open('data/%s_workflow.dat' % k, 'a') as f:
            f.write("%s\t%i\n" % (project, len(workflow[k])))


def to_latex(workflow):
    def get_enumeration(key):
        return '''
        \\textbf{\\textit{%s}}
        \\begin{enumerate}[topsep=0pt,itemsep=-2pt,leftmargin=13pt]
        ''' % key + "\n".join("\item " + i for i in workflow[key]) + '''
        \end{enumerate}
        '''

    return '''
    \\begin{tabular}[t]{@{}>{\\raggedright\\arraybackslash}p{0.25\\textwidth}}
    \\textbf{\\textbf{LHSNet}}\\\\
    ''' + "".join(get_enumeration('Creation')) + "".join(get_enumeration('Revision')) + "".join(get_enumeration('Application')) + '''
    \end{tabular}
    '''

def parse_workflow(file):
    workflows = {}

    with open(file, 'r') as f:

        current = None
        for l in f.readlines():
            l = l.strip()
            if not l:
                pass

            if l.startswith('*'):
                if current not in workflows:
                    workflows[current] = []

                l = l.lstrip('*').strip()
                workflows[current].append(l)
            else:
                current = l

    return workflows