#@+leo-ver=5-thin
#@+node:peckj.20131203081434.4591: * @file TreeMap.py
#@@language python
#@@tabwidth -2
#@+others
#@+node:peckj.20131203081434.4592: ** Map declarations
""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import string
import rbtree
#@+node:peckj.20131203081434.4610: ** class TreeMap (ex. 3.5)
class TreeMap():
    #@+others
    #@+node:peckj.20131203081434.4611: *3* __init__
    def __init__(self):
      self.map = rbtree.rbtree()
    #@+node:peckj.20131203081434.4612: *3* add
    def add(self, k, v):
      self.map[k] = v
    #@+node:peckj.20131203081434.4613: *3* get
    def get(self, k):
      return self.map[k]
    #@-others
#@+node:peckj.20131203081434.4609: ** main
def main(script):
    m = TreeMap()
    s = string.ascii_lowercase

    for k, v in enumerate(s):
        m.add(k, v)

    for k in range(len(s)):
        print k, m.get(k)


#@-others
if __name__ == '__main__':
    import sys
    main(*sys.argv)
#@-leo
