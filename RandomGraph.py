#@+leo-ver=5-thin
#@+node:peckj.20131202180255.3747: * @file RandomGraph.py
#@@language python
#@@tabwidth -2

#@+<< imports >>
#@+node:peckj.20131202180255.3748: ** << imports >>
from Graph import Graph
from Graph import Vertex
from Graph import Edge

import random
import itertools
#@-<< imports >>
#@+others
#@+node:peckj.20131202180255.3749: ** class RandomGraph
class RandomGraph(Graph):
  #@+others
  #@+node:peckj.20131202180255.3750: *3* add_random_edges (ex. 2.4)
  def add_random_edges(self, p):
    for e1,e2 in itertools.combinations(self.vertices(), 2):
      if random.random() <= p:
        self.add_edge(Edge(e1,e2))
  #@-others
#@+node:peckj.20131202180255.3751: ** main
def main():
  vertices = [Vertex(x) for x in ['a', 'b', 'c', 'd', 'e']]
  g = RandomGraph(vertices, [])
  g.add_random_edges(0.1)
  print g
#@-others

if __name__=='__main__':
  main()
#@-leo
