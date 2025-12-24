class Node:
    def __init__(self,value):
        self.next= None
        self.value=value

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self._size=0
    
    def enqueue(self, value):
        new_node=Node(value)
        if not self._size:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self._size+=1
        return new_node.value
    
    def dequeue(self):
        if not self._size:
            raise Exception("Queue is empty")
        former_head=self.head
        self.head=self.head.next
        former_head.next=None
        self._size-=1
        if not self._size:
            self.tail=None #resets the tail now that the list is empty
        return former_head.value
    

    def clear(self):
        self.head=None
        self.tail=None
        self._size=0
        return self
    
    def peek(self):
        return self.head.value
    

sample=Queue()

sample.enqueue(5)
sample.enqueue(5)
sample.enqueue(5)