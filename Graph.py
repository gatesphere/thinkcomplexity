#@+leo-ver=5-thin
#@+node:peckj.20131202081144.4747: * @file Graph.py
#@@language python

#@+<< docstring >>
#@+node:peckj.20131202081144.4748: ** << docstring >>
""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
#@-<< docstring >>

#@+others
#@+node:peckj.20131202081144.4749: ** class Vertex
class Vertex(object):
    """A Vertex is a node in a graph."""

    #@+others
    #@+node:peckj.20131202081144.4750: *3* __init__
    def __init__(self, label=''):
        self.label = label
    #@+node:peckj.20131202081144.4751: *3* __repr__
    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)
    #@-others
    
    __str__ = __repr__
    """The str and repr forms of this object are the same."""
#@+node:peckj.20131202081144.4752: ** class Edge
class Edge(tuple):
    """An Edge is a list of two vertices."""

    #@+others
    #@+node:peckj.20131202081144.4753: *3* __new__
    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)
    #@+node:peckj.20131202081144.4754: *3* __repr__
    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))
    #@-others
    
    __str__ = __repr__
    """The str and repr forms of this object are the same."""
#@+node:peckj.20131202081144.4755: ** class Graph
class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    #@+others
    #@+node:peckj.20131202081144.4756: *3* __init__
    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)
    #@+node:peckj.20131202081144.4757: *3* add_vertex
    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}
    #@+node:peckj.20131202081144.4758: *3* add_edge
    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
    #@+node:peckj.20131202081144.4760: *3* get_edge (ex. 2.2.3)
    def get_edge(self, v1, v2):
        ''' returns the edge connecting two verticies, or None if 
            no such edge exists
        '''
        try:
          e = self[v1][v2]
          return e
        except:
          return None
    #@+node:peckj.20131202081144.4761: *3* remove_edge (ex. 2.2.4)
    def remove_edge(self, e):
      v,w = e
      del self[v][w]
      del self[w][v]
    #@+node:peckj.20131202081144.4762: *3* vertices (ex. 2.2.5)
    def vertices(self):
      return self.keys()
    #@+node:peckj.20131202081144.4763: *3* edges (ex. 2.2.6)
    def edges(self):
      edgelist = []
      for i in self.keys():
        for x in self[i].keys():
          edgelist.append(self[i][x])
      return list(set(edgelist)) # ugly, slow hack to return a unique list
    #@+node:peckj.20131202180255.3694: *3* out_vertices (ex. 2.2.7)
    def out_vertices(self, v):
      return self[v].keys()
    #@+node:peckj.20131202180255.3701: *3* out_edges (ex. 2.2.8)
    def out_edges(self, v):
      edgelist = []
      for x in self[v].keys():
        edgelist.append(self[v][x])
      return edgelist
    #@+node:peckj.20131202180255.3704: *3* add_all_edges (ex. 2.2.9)
    def add_all_edges(self):
      ''' from an edgeless graph, it creates a complete graph '''
      import itertools
      for e1,e2 in itertools.combinations(self.vertices(), 2):
        self.add_edge(Edge(e1,e2))
    #@+node:peckj.20131202180255.3746: *3* add_regular_edges (ex. 2.3)
    def add_regular_edges(self, n):
        ''' converts an edgeless graph to a n-regular graph 
            (i.e. all vertices have the same number of edges) 
        '''
        if n < 0 or n >= len(self.vertices()):
            raise ValueError, '0 <= n < len(self.vertices()) must be true.'
        vs = self.vertices()
        if len(vs)%2 != 0 and n%2 != 0:
            raise ValueError, 'Cannot construct a n-regular graph with odd vertices and odd n'
        for i in range(len(vs)):
            start = i+1
            print '%s -> %s' % (i, start)
            for j in range(n/2):
                if start+j > len(vs)-1: start -= len(vs)
                t = start+j
                self.add_edge(Edge(vs[i], vs[t]))
        if n%2 != 0: # n is odd
          # connect additionally to vertex directly opposite
          for i in range(len(vs)):
              self.add_edge(Edge(vs[i], vs[i-len(vs)/2]))
    #@+node:peckj.20131202180255.3752: *3* is_connected (ex. 2.5)
    def is_connected(self):
      workqueue = [self.vertices()[0]]
      seen = []
      while len(workqueue) > 0:
        v = workqueue[0]
        workqueue = workqueue[1:]
        seen.append(v)
        for n in self[v].keys():
          if n not in seen and n not in workqueue:
            workqueue.append(n)
      return len(seen) == len(self.vertices())
    #@-others

#@+node:peckj.20131202081144.4759: ** main
def main(script, *args):
    #@+others
    #@+node:peckj.20131202180255.3695: *3* basic tests
    print 'basic tests'
    v = Vertex('v')
    print "vertex v:", v
    w = Vertex('w')
    print "vertex w:", w
    e = Edge(v, w)
    print "edge e:", e
    g = Graph([v,w], [e])
    print "graph g:", g
    #@+node:peckj.20131202180255.3696: *3* edges
    print
    print 'edges'
    print "edges:", g.edges()
    #@+node:peckj.20131202180255.3697: *3* get_edge
    print
    print 'get_edge'
    edge = g.get_edge(v,w)
    print "edge:", edge
    edge = g.get_edge(w,v)
    print "edge:", edge
    edge = g.get_edge(v,Vertex('q'))
    print "edge:", edge
    #@+node:peckj.20131202180255.3698: *3* remove_edge
    print
    print 'remove_edge'
    g.remove_edge(e)
    print "graph g:", g
    #@+node:peckj.20131202180255.3699: *3* vertices
    print
    print 'vertices'
    print "g.vertices:", g.vertices()
    #@+node:peckj.20131202180255.3700: *3* out_vertices
    print
    print 'out_vertices'
    g.add_edge(e)
    print g.out_vertices(v)
    #@+node:peckj.20131202180255.3703: *3* out_edges
    print
    print 'out_edges'
    print g.out_edges(v)
    #@+node:peckj.20131202180255.3706: *3* add_all_edges
    print
    print 'add_all_edges'
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    g = Graph([v,w,x,y],[])
    print "graph g:", g
    g.add_all_edges()
    print "graph g:", g
    #@+node:peckj.20131202180255.3754: *3* is_connected
    print
    print 'is_connected'
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    g = Graph([v,w,x,y],[])
    print "graph g:", g
    print 'is_connected:', g.is_connected()
    g.add_all_edges()
    print "graph g:", g
    print 'is_connected:', g.is_connected()
    #@-others
#@-others

if __name__ == '__main__':
    import sys
    main(*sys.argv)
#@-leo
