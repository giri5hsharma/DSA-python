class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value): #complexity is O(1) as we just change the tail
        new_node= Node(value)
        if not self.length: #works if the list is empty
            self.head=self.tail=new_node 
        else:
            self.tail.next= new_node #doesnt work on empty list
            self.tail=new_node
        self.length += 1
        return self
    
    def prepend(self,value): #complexity is O(1) as we just change the head
        new_node=Node(value)
        if not self.length: #works if the list is empty
            self.head=self.tail= new_node
        else:
            new_node.next= self.head #makes the current head the next link 
            self.head= new_node #makes the added element the new head
        self.length+=1
        return self
    
    def popleft(self): #complexity is O(1) as we just change the head
        if not self.length:
            raise Exception("List was empty")
        temp_node= self.head #saves the current head
        self.head=temp_node.next #makes the next node the new head
        temp_node.next=None #clears the next link of the old head
        self.length-=1 
        if not self.length:
            self.tail=None  #checks if list is now empty
        return temp_node.value
    

    def popright(self): #complexity is O(n) as we have to traverse the list
        if not self.length:
            raise Exception("List already empty!")
        tail_value=self.tail.value
        if self.length==1:
            self.head=self.tail=None
        else:
            temp_node=self.head
            while temp_node.next!=self.tail:
                temp_node=temp_node.next
            self.tail=temp_node
            self.tail.next=None
        self.length-=1
        return tail_value
    
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
            self.tail=previous_node
        #remove the current node
        previous_node.next=current_node.next
        current_node.next=None
        self.length-=1
        return current_node.value #returns the removed value

    def reverse(self):
        if self.length<2:
            return self
        left_node= None
        middle_node= self.head
        right_node=middle_node.next
        while middle_node != None:
            middle_node.next=left_node
            left_node=middle_node
            middle_node=right_node
            right_node=right_node.next
        self.head, self.tail = self.tail, self.head
        return self