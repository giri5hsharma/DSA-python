class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def append(self,value):
        new_element=Node(value)
        if not self.size:
            self.head=self.tail=new_element
        else:
            self.tail.next=new_element
            self.tail=new_element
        self.size+=1
        return self
    
    def pop_left(self):
        if not self.size:
            raise Exception("Linked List is empty")
        else:
            popped_head=self.head
            self.head=self.head.next
        self.size-=1
        return popped_head
    
    def prepend(self,value):
        new_element=Node(value)
        if not self.size:
            self.head=self.tail=new_element
        else:
            new_element.next=self.head
            self.head=new_element
        self.size+=1
        return self