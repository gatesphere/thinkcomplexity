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
import string
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
#@+node:peckj.20131203081434.3831: ** test_p (ex. 2.6)
def test_p(n, p, num):
  labels = string.lowercase + string.uppercase + string.punctuation
  count = 0
  for i in range(num):
    vs = [Vertex(c) for c in labels[:n]]
    g = RandomGraph(vs,[])
    g.add_random_edges(p)
    if g.is_connected(): count += 1
  return count
      
#@+node:peckj.20131202180255.3751: ** main
def main(script, n=26, p=0.1, num=1, *args):
  n = int(n)
  p = float(p)
  num = int(num)
  count = test_p(n, p, num)
  print count
#@-others

if __name__=='__main__':
  import sys
  main(*sys.argv)
#@-leo
