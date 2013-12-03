#@+leo-ver=5-thin
#@+node:peckj.20131203081434.4553: * @file Map.py
#@@language python
#@@tabwidth -2
#@+others
#@+node:peckj.20131203081434.4554: ** Map declarations
""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import string


#@+node:peckj.20131203081434.4555: ** class LinearMap
class LinearMap(object):
    """A simple implementation of a map using a list of tuples
    where each tuple is a key-value pair."""


#@+node:peckj.20131203081434.4559: *3* __init__
def __init__(self):
    self.items = []
#@+node:peckj.20131203081434.4560: *3* add
def add(self, k, v):
    """Adds a new item that maps from key (k) to value (v).
    Assumes that they keys are unique."""
    self.items.append((k, v))
#@+node:peckj.20131203081434.4561: *3* get
def get(self, k):
    """Looks up the key (k) and returns the corresponding value,
    or raises KeyError if the key is not found."""
    for key, val in self.items:
        if key == k:
            return val
    raise KeyError
#@+node:peckj.20131203081434.4556: ** class BetterMap
class BetterMap(object):
    """A faster implementation of a map using a list of LinearMaps
    and the built-in function hash() to determine which LinearMap
    to put each key into."""
#@+node:peckj.20131203081434.4562: *3* __init__
def __init__(self, n=100):
    """Appends (n) LinearMaps onto (self)."""
    self.maps = []
    for i in range(n):
        self.maps.append(LinearMap())
#@+node:peckj.20131203081434.4570: *3* __len__ (ex. 3.4.1)
def __len__(self):
  return len(self.maps)
#@+node:peckj.20131203081434.4563: *3* find_map
def find_map(self, k):
    """Finds the right LinearMap for key (k)."""
    index = hash(k) % len(self.maps)
    return self.maps[index]
#@+node:peckj.20131203081434.4571: *3* iteritems (ex. 3.4.2)
def iteritems(self):
  for m in self.maps:
    yield m
#@+node:peckj.20131203081434.4564: *3* add
def add(self, k, v):
    """Adds a new item to the appropriate LinearMap for key (k)."""
    m = self.find_map(k)
    m.add(k, v)
#@+node:peckj.20131203081434.4565: *3* get
def get(self, k):
    """Finds the right LinearMap for key (k) and looks up (k) in it."""
    m = self.find_map(k)
    return m.get(k)
#@+node:peckj.20131203081434.4557: ** class HashMap
class HashMap(object):
    """An implementation of a hashtable using a BetterMap
    that grows so that the number of items never exceeds the number
    of LinearMaps.

    The amortized cost of add should be O(1) provided that the
    implementation of sum in resize is linear."""



#@+node:peckj.20131203081434.4566: *3* __init__
def __init__(self):
    """Starts with 2 LinearMaps and 0 items."""
    self.maps = BetterMap(2)
    self.num = 0
#@+node:peckj.20131203081434.4567: *3* get
def get(self, k):
    """Looks up the key (k) and returns the corresponding value,
    or raises KeyError if the key is not found."""
    return self.maps.get(k)
#@+node:peckj.20131203081434.4568: *3* add
def add(self, k, v):
    """Resize the map if necessary and adds the new item."""
    if self.num == len(self.maps):
        self.resize()

    self.maps.add(k, v)
    self.num += 1
#@+node:peckj.20131203081434.4569: *3* resize
def resize(self):
    """Makes a new map, twice as big, and rehashes the items."""
    new_maps = BetterMap(self.num * 2)

    for m in self.maps.iteritems():
        for k, v in m.items:
            new_maps.add(k, v)

    self.maps = new_maps
#@+node:peckj.20131203081434.4558: ** main
def main(script):
    m = HashMap()
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
