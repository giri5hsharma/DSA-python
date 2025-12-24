class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self._length=0
    
    def append(self,value):
        new_node= Node(value)
        if not self._length:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self._length+=1
        return self
    
    def prepend(self,value):
        new_node= Node(value)
        if not self._length:
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self._length+=1
        return self
    

    def popleft(self):
        if not self._length:
            return None
        last_head= self.head #REASSIGN OLD HEAD TO VARIABLE
        if self._length==1:
            self.head=self.tail=None
        else:
            self.head= self.head.next #DEFINE NEW HEAD
            last_head.next=None #REMOVE OLD HEAD COMPLETELY
            self.head.prev=None #NEW HEAD BACKWARDS LINKAGE
        self._length-=1
        return last_head.value #RETURNS THE REMOVED ELEMENT
    
    def popright(self):
        if not self._length:
            return None
        last_tail=self.tail
        if self._length==1:
            self.head=self.tail=None
        else:
            self.tail=last_tail.prev
            last_tail.prev=None
            self.tail.next=None
        self._length-=1
        return last_tail.value
