#@+leo-ver=5-thin
#@+node:peckj.20131203081434.3832: * @file AlphaNumGenerator.py
#@@language python

import string

#@+others
#@+node:peckj.20131203081434.3833: ** alphanum_gen (ex. 2.7)
def alphanum_gen():
  i = 1
  while True:
    for c in string.lowercase:
      yield '%s%s' % (c,i)
    i += 1
#@+node:peckj.20131203081434.3834: ** main
def main(script, *args):
  i = 0
  for c in alphanum_gen():
    print c
    i += 1
    if i == 200:
      break
#@-others

if __name__=='__main__':
  import sys
  main(*sys.argv)
#@-leo
