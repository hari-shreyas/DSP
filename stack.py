class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print('added element:',element)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            print('The stack is empty')
        else:
            removed_element = self.stack.pop()
            print('removed element:', removed_element)
            return removed_element

    def peek(self):
        if self.is_empty():
            print('The stack is empty')
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print('The stack is empty')
        else:
            print('Current stack:', self.stack)


s = Stack()
s.push(str(3))
s.push(str(8))
s.push(str(25))
s.display()  # Display the stack
print('Top element:', s.peek())  
print('Stack size:', s.size()) 
s.pop()  
s.display()  
