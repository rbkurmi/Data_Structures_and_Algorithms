class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = 1 + max(height(node.left), height(node.right))
    balance = getBalance(node)
    if balance > 1 and key < node.left.key:
        return rightRotate(node)
    if balance < -1 and key > node.right.key:
        return leftRotate(node)
    if balance > 1 and key > node.left.key:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    if balance < -1 and key < node.right.key:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node

def height(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def rightRotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def leftRotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def preorder(root):
    if not root:
        return
    print(root.key, end=" ")
    preorder(root.left)
    preorder(root.right)

# Usage
root = None
nums = [10, 20, 30, 40, 50, 25]
for num in nums:
    root = insert(root, num)
print("Preorder traversal of the AVL tree:")
preorder(root)
