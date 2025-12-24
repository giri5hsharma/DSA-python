class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node= Node(value)
        if not self.length: #works if the list is empty
            self.head=self.tail=new_node 
        else:
            self.tail.next= new_node #doesnt work on empty list
            self.tail=new_node
        self.length += 1
        return self
    
    def prepend(self,value):
        new_node=Node(value)
        if not self.length: #works if the list is empty
            self.head=self.tail= new_node
        else:
            new_node.next= self.head #makes the current head the next link 
            self.head= new_node #makes the added element the new head
        self.length+=1
        return self


my_list= SinglyLinkedList()

my_list.append(5)
my_list.append(5)
my_list.append(10)

print(my_list.head.value)
print(my_list.tail.value)
print(my_list.length)


my_list.prepend(69)

print(my_list.head.value)
print(my_list.tail.value)
print(my_list.length)