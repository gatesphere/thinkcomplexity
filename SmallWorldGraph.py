#@+leo-ver=5-thin
#@+node:peckj.20131211141232.3877: * @file SmallWorldGraph.py
#@@language python

#@+<< imports >>
#@+node:peckj.20131211141232.3878: ** << imports >>
from RandomGraph import RandomGraph
from Graph import Vertex
from Graph import Edge

import random
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20131211141232.3879: ** << declarations >>
#@-<< declarations >>

#@+others
#@+node:peckj.20131211141232.3881: ** class SmallWorldGraph
class SmallWorldGraph(RandomGraph):
  #@+others
  #@+node:peckj.20131211141232.3883: *3* __init__
  def __init__(self, n, k):
    self.n = n
    self.k = k
    for i in range(n):
      self.add_vertex(Vertex(str(i)))
    self.add_regular_edges(k)
  #@+node:peckj.20131211141232.3882: *3* rewire
  def rewire(self, p):
    ''' steps of the original algorithm on an n-node k-regular graph:
        for i in k/2:
          for each node n:
            for each edge x that connects n to n+i or n-i:
              with probability p:
                remove edge x
                reroute edge x to another node with uniform probability
                add edge x if it does not already exist
    '''
    for e in self.edges()[:]:
      if random.random() <= p:
        v1, v2 = e
        otherv = random.choice(self.vertices())
        if not self.get_edge(v1, otherv):
          self.remove_edge(e)
          self.add_edge(Edge(v1,otherv))
  #@+at
  #   for i in range(1,self.k/2+1):
  #     vs = self.vertices()
  #     for n in range(len(vs)):
  #       #print 'n:', n, 'i:', i, 'n-i:', n-i, 'len(vs)-i+n:', len(vs)-n+i
  #       v = vs[n]
  #       vprev = vs[n-i]
  #       if n+i >= len(vs):
  #         vnext = vs[n+i-len(vs)]
  #       else:
  #         vnext = vs[n+i]
  #       print 'v:', v.label, 'vnext:', vnext.label, 'vprev:', vprev.label
  #       for vn in [vprev, vnext]:
  #         if random.random() <= p:
  #           otherv = random.choice(self.vertices())
  #           if not self.get_edge(v,otherv):
  #             self.remove_edge(self[v][vn])
  #             self.add_edge(Edge(v,otherv))
  # 
  #           
  #         
  #@-others
#@+node:peckj.20131211141232.3880: ** main
def main():
  pass
#@-others

if __name__=='__main__':
  main()
#@-leo
