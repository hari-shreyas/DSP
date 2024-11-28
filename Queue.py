class queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,item):
        self.q.append(item)
        print('added element:',item)
    def is_empty(self):
        return len(self.q)==0
    def dequeue(self):
        if self.is_empty():
            print ('queue is empty')
        else:
            self.q.pop(0)
            print ('removed element. the new queue is:',self.q)
    def front(self):
        print ('first element:',self.q[0])
    def size(self):
        print ('size of queue:',len(self.q))
    def display(self):
        if self.is_empty():
            print ('queue is empty')
        else:
            print ('the queue is:', self.q)
a=queue()
a.enqueue(15)
a.enqueue(10)
a.enqueue(25)
a.display()
a.dequeue()
a.front()
a.size()
