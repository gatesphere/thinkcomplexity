#@+leo-ver=5-thin
#@+node:peckj.20131202180255.3742: * @file GraphTest.py
#@@language python

#@+<< imports >>
#@+node:peckj.20131202180255.3743: ** << imports >>
from Graph import Vertex
from Graph import Edge
from Graph import Graph
from GraphWorld import GraphWorld
from GraphWorld import CircleLayout

import string
#@-<< imports >>

#@+others
#@+node:peckj.20131202180255.3744: ** main
def main(n='18'):
    # create n Vertices
    n = int(n)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = Graph(vs)
    #g.add_all_edges()
    g.add_regular_edges(16)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
#@-others

if __name__ == '__main__':
   main()
#@-leo
