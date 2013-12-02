#@+leo-ver=5-thin
#@+node:peckj.20131202081144.4720: * @file GraphCode.py
#@@language python

#@+<< docstring >>
#@+node:peckj.20131202081144.4721: ** << docstring >>
""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
#@-<< docstring >>

#@+others
#@+node:peckj.20131202081144.4722: ** class Vertex
class Vertex(object):
    """A Vertex is a node in a graph."""

    #@+others
    #@+node:peckj.20131202081144.4726: *3* __init__
    def __init__(self, label=''):
        self.label = label
    #@+node:peckj.20131202081144.4727: *3* __repr__
    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)
    #@-others
    
    __str__ = __repr__
    """The str and repr forms of this object are the same."""
#@+node:peckj.20131202081144.4723: ** class Edge
class Edge(tuple):
    """An Edge is a list of two vertices."""

    #@+others
    #@+node:peckj.20131202081144.4728: *3* __new__
    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)
    #@+node:peckj.20131202081144.4729: *3* __repr__
    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))
    #@-others
    
    __str__ = __repr__
    """The str and repr forms of this object are the same."""
#@+node:peckj.20131202081144.4724: ** class Graph
class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    #@+others
    #@+node:peckj.20131202081144.4730: *3* __init__
    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)
    #@+node:peckj.20131202081144.4731: *3* add_vertex
    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}
    #@+node:peckj.20131202081144.4733: *3* add_edge
    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
    #@-others

#@+node:peckj.20131202081144.4725: ** main
def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w], [e])
    print g
#@-others

if __name__ == '__main__':
    import sys
    main(*sys.argv)
#@-leo
