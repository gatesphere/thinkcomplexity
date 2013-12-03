#@+leo-ver=5-thin
#@+node:peckj.20131203081434.4547: * @file BisectSearch.py
#@@language python

#@+<< imports >>
#@+node:peckj.20131203081434.4548: ** << imports >>
import math
#@-<< imports >>
#@+others
#@+node:peckj.20131203081434.4552: ** bisect (ex. 3.3)
def bisect(l, target):
  max_iter = int(math.sqrt(len(l))) # it will run in O(log n)
  min = 0
  max = len(l)
  for i in range(max_iter):
    mid = min + ((max-min)/2)
    if l[mid] == target:
      return mid
    elif l[mid] < target:
      min = mid+1
    elif l[mid] > target:
      max = mid-1
  return None
#@+node:peckj.20131203081434.4549: ** main
def main(script, *args):
  target = 19875
  l = list(range(0,20000))
  l2 = list(range(0,20000))
  del l2[target]
  
  print bisect(l, target)
  print bisect(l2, target)

  
  
#@-others

if __name__=='__main__':
  import sys
  main(*sys.argv)
#@-leo
