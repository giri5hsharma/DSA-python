class Node:
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
        if not self.length:
            self.head=self.tail=new_node
        else:
            self.tail.next= new_node #doesnt work on empty list
            self.tail=new_node
        self.length += 1
        return self

my_list= SinglyLinkedList()
print(my_list)
print(my_list.head)
print(my_list.tail)
print(my_list.length)

print(my_list.append(1))
print(my_list.append(3))
print(my_list.append(5))
print(my_list.append(3))

print(my_list.head.value)
print(my_list.tail.value)
print(my_list.length)