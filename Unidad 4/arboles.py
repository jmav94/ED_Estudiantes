class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
    
    # Recorrido en orden (inorder)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)



#BST
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        if value < self.value:
           if self.left is None:
               self.left = BSTNode(value)
           else:
               self.left.insert(value)
        else:
           if self.right is None:
               self.right = BSTNode(value)
           else:
               self.right.insert(value)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value, end=' ')
        if self.right:
            self.right.inorder()



# emplos de uso

# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)

# print("Recorrido en orden:")
# tree.inorder(tree.root)


# tree1 = BinaryTree('A')
# tree1.root.left = Node('B')
# tree1.root.right = Node('C')
# tree1.root.left.left = Node('D')
# tree1.root.left.right = Node('E')
# tree1.root.right.left = Node('F')

# print("\nRecorrido en orden del segundo árbol:")
# tree1.inorder(tree1.root)


root = BSTNode(10)
for n in [5,15,3,7,12,17]:
    root.insert(n)


root.inorder()

