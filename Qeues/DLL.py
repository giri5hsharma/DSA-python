class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self._size=0
    
    def enqueue(self,value):
        new_node=Node(value)
        if not self._size:
            self.head=self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        self._size+=1
        return new_node.value
    
    def dequeue(self):
        if not self._size:
            raise Exception("Queue is empty")
        
        former_head=self.head
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        else:
            self.tail=None #queue becomes empty
        former_head.next=None
        self._size-=1
        return former_head.value
    
    def size(self):
        return self._size
    
    def peek(self):
        if not self._size:
            raise Exception("Queue is empty")
        return self.head.value

            