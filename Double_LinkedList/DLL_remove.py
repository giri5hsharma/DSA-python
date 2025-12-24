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
            new_node.prev= self.tail
            self.tail=new_node
        self._length+=1
        return self
    
    def prepend(self,value):
        new_node=Node(value)
        if not self._length:
            self.head=self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self._length+=1
        return self
    
    def popright(self):
        if not self._length:
            return None
        last_tail=self.tail
        if self._length==1:
            self.head=self.tail=None
        else:
            self.tail= self.tail.prev
            self.tail.next=None
        self._length-=1
        return last_tail.value
    
    
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
    
    def remove(self, value): #complexity is O(n) as we have to traverse the list
        if not self.length:
            raise Exception("List is empty")
        if self.head.value == value:
            return self.popleft()
        previous_node= self.head
        current_node= self.head.next
        while current_node!=None and current_node.value!=value:
            previous_node=current_node
            current_node=current_node.next
        if current_node==None:
            raise ValueError("item not in list")
        if current_node.next==None: #update tail if removing the last element
            return self.popright()
        #remove the current node
        current_node.next.prev=current_node.prev #SETS THE PREVIOUS NODE OF THE NEXT NODE TO THE ONE BEFORE CURRENT NODE
        current_node.previous.next=current_node.next #SETS THE NEXT NODE OF THE PREVIOUS NODE TO THE ONE AFTER CURRENT NODE
        #remove this shit from the list
        current_node.next=None 
        current_node.prev=None 

        self._length-=1
        return current_node.value #returns the removed value

