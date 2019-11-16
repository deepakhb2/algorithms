class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.root.__dict__)

    def insert(self, value):
        new_node = Node(value)
        if(not self.root):
            self.root = new_node
        else:
            current_node = self.root
            while(True):
                if(value < current_node.value):
                    if(not current_node.left):
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    if(not current_node.right):
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        if(not self.root):
            return False
        current_node = self.root
        while(current_node):
            if(value < current_node.value):
                current_node = current_node.left
            elif(value > current_node.value):
                current_node = current_node.right
            elif(current_node.value == value):
                return current_node
        return False

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(3)
tree.insert(10)
tree.insert(5)
tree.insert(6)
print(tree)
print(tree.lookup(6).value)
print(tree.lookup(100))
