class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        new_node= Node(value)

        if not self.root:
            self.root=new_node
            return self
        
        current_node=self.root #condtion if the root node exists

        while(value != current_node.value):
            if value<current_node.value:
                if not current_node.left:
                    current_node.left= new_node
                    break
                current_node= current_node.left
            else:
                if not current_node.right:
                    current_node.right=new_node
                    break
                current_node=current_node.right
        
        return self


