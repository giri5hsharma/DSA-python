class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class Stack:
    def __init__(self):
        self._top=None
        self._size=0
        self._max_capacity= 10
    
    def push(self,value):
        if self._max_capacity== self._size:
            raise Exception("Size limit of stack exceeded")
        new_element= Node(value)
        new_element.next= self._top
        self._top=new_element
        self._size+=1
        return self
    
    def display(self):
        current = self._top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print()
    
    def pop(self):
        if self._size==0:
            raise Exception("Stack is empty")
        last_top=self._top #store it in var for callback and later use
        self._top=self._top.next
        last_top.next=None #separting the last top from the list
        self._size-=1
        return last_top.value
    
    def peek(self): #used to check the value of the top node
        if not self._size:
            raise Exception("Stack is empty")
        return self._top.value
    
    def clear(self):
        self._size=0
        self._top=None
        return self
    
    def __len__(self):
        return self._size
    


damn= Stack()

print(damn.push(10))
print(damn.push(20))
print(damn.push(30))

damn.display()

print(damn.peek())

print(damn.pop())
print(damn.pop())

print(damn.peek())

print(damn.pop())


