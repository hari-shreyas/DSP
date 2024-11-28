class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlylinkedlist:
    def __init__(self):
        self.head=None
    def AddBeg(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    
    def AddEnd(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
    
    def AddAfter(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
        if n is None:
            print ('element not in list')
        else:
            new_node=node(data)
            new_node.next=n.next
            n.next=new_node
    
    def display(self):
        current=self.head
        while current:
            print (current.data,end=' ')
            current=current.next
sll=singlylinkedlist()
sll.AddBeg(5)
sll.AddBeg(10)
sll.AddBeg(15)
sll.AddEnd(20)
sll.AddAfter(17,15)
sll.display()