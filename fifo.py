#@+leo-ver=5-thin
#@+node:peckj.20131211141232.3867: * @file fifo.py
#@@language python

#@+<< imports >>
#@+node:peckj.20131211141232.3868: ** << imports >>
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20131211141232.3869: ** << declarations >>
#@-<< declarations >>

#@+others
#@+node:peckj.20131211141232.3870: ** class Fifo
class Fifo:
  #@+others
  #@+node:peckj.20131211141232.3874: *3* __init__
  def __init__(self):
    self.head = None
    self.tail = None
  #@+node:peckj.20131211141232.3872: *3* append
  def append(self, value):
    ''' add value to back of the queue '''
    if self.head is None:
      # first item added
      n = FifoNode(value, None, None)
      self.head = n
      self.tail = n
    else:
      # add to list
      n = FifoNode(value, self.tail, None)
      self.tail.next = n
      self.tail = n
  #@+node:peckj.20131211141232.3873: *3* pop
  def pop(self):
    ''' return value from front of queue '''
    if self.head is None:
      return None
    v = self.head
    self.head = v.next
    self.head.prev = None
    return v.value
  #@+node:peckj.20131211141232.3876: *3* display
  def display(self):
    n = self.head
    vals = []
    while n is not None:
      vals.append(n.value)
      n = n.next
    print "H-->",vals,"<--T"
  #@-others
#@+node:peckj.20131211141232.3871: ** class FifoNode
class FifoNode():
  def __init__(self, value, prev, next):
    self.value = value
    self.prev = prev
    self.next = next
#@+node:peckj.20131211141232.3875: ** main
def main():
  q = Fifo()
  q.display()
  q.append(1)
  q.append(2)
  q.append(3)
  q.display()
  q.pop()
  q.display()
  q.pop()
  q.display()
#@-others

if __name__=='__main__':
  main()
#@-leo
