#@+leo-ver=5-thin
#@+node:peckj.20131211141232.3887: * @file SmallWorldGraphTest.py
#@@language python

#@+<< imports >>
#@+node:peckj.20131211141232.3888: ** << imports >>
from SmallWorldGraph import SmallWorldGraph
from GraphWorld import GraphWorld
from GraphWorld import CircleLayout

import string
#@-<< imports >>

#@+others
#@+node:peckj.20131211141232.3889: ** main
def main(n='20', k='4', p='0.4'):
    n = int(n)
    k = int(k)
    p = float(p)
    g = SmallWorldGraph(n, k)
    g.rewire(p)

    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
#@-others

if __name__ == '__main__':
   main()
#@-leo
