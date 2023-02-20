class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, node):
        if node is None:
            return False
        elif val == node.val:
            return True
        elif val < node.val:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)

bst = BST()

bst.insert(5)
bst.insert(2)
bst.insert(13)
bst.insert(1)
bst.insert(4)
bst.insert(10)
bst.insert(15)

print(bst.search(4))  # True
print(bst.search(7))  # False
