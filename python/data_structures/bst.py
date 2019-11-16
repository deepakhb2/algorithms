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

    def remove(self, value):
        if(not self.root):
            return False
        current_node = self.root
        parent_node = None
        while(current_node):
            if(value < current_node.value):
                parent_node = current_node
                current_node = current_node.left
            elif(value > current_node.value):
                parent_node = current_node
                current_node = current_node.right
            elif(current_node.value == value):
                # If no right child
                if(not current_node.right):
                    if(not parent_node):
                        self.root = current_node.left
                    else:
                        if(current_node.value < parent_node.value):
                            parent_node.left = current_node.left
                        elif(current_node.value > parent_node.value):
                            parent_node.right = current_node.left
                # Right child which doesn't have left child
                elif(not current_node.right.left):
                    if(not parent_node):
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left
                        if(current_node.value < parent_node.value):
                            parent_node.left = current_node.right
                        elif(current_node.value > parent_node.value):
                            parent_node.right = current_node.right
                # Right child that has a left child
                else:
                    # Find the right child's left most child.
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while(not leftmost.left):
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree.
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if(not parent_node):
                        self.root = leftmost
                    else:
                        if(current_node.value < parent_node.value):
                            parent_node.left = lefmost
                        elif(current_node.value > parent_node.value):
                            parent_node.right = leftmost
            return True

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
print(tree.remove(9))
print(tree)
