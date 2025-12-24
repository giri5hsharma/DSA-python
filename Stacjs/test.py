class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class Stack:
    def __init__(self):
        self.top=None
        self.size=0
        self.max_size=10
    
    def push(self,value):
        if self.size==self.max_size:
            raise Exception("Stack is full")
        element=Node(value)
        element.next=self.head
        self.head=element
        self.size+=1
        return self
    
    def pop(self):
        if not self.size:
            raise Exception("stack is empty")
        last_top=self.head
        self.head=self.head.next
        self.size-=1
        return last_top.value
    
    def peek(self):
        if not self.size:
            raise Exception("Stack is empty")
        return self.head.value

    def disp(self):
        if not self.size:
            raise Exception("stack is empty")
        currnet=self.head
        while currnet:
            print(f"{currnet.value} -> ")
            currnet=currnet.next
        print("None")