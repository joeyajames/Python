
# implemented by Linked list
class Node(object):
  def __init__(self, item = None):
    self.item = item
    self.next = None
    self.previous = None


class Queue(object):
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def enqueue(self, x):
    newNode = Node(x)
    if self.head == None:
      self.head = self.tail = newNode
    else:
      self.tail.next = newNode
      newNode.previous = self.tail
      self.tail = newNode
    self.length += 1


  def dequeue (self):
    item = self.head.item
    self.head = self.head.next 
    self.length -= 1
    if self.length == 0:
      self.last = None
    return item


#################################################

# implemented by array
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
    
    def display(self):
        ar = []
        for i in self.items:
            ar.append(i)
        return ar
que = Queue()
que.enqueue('google')
que.enqueue('youtube')
que.enqueue('udemy')
que.enqueue('udacity')
que.dequeue()
que.dequeue()
print(que.display())
