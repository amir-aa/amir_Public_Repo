class Node:
    def __init__(self,value:int) -> None:
        self.right=None
        self.left=None
        self.value=value

class Tree:
    def __init__(self) -> None:
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root,value)
    def _insert(self,currentNode:Node,value):
        if value<currentNode.value:
            if currentNode.left is None:
                currentNode.left= Node(value)
            else:
                self._insert(currentNode.left,value)
        elif value>currentNode.value:
            if currentNode.right is None:
                currentNode.right=Node(value)
            else:
                self._insert(currentNode.right,value)
        else:
            print("Duplicate Value")
        
    def printTree(self):
        self._printTree(self.root,0)
    def _printTree(self,node:Node,level):
        if node is not None:
            self._printTree(node.right,level+1)
            print('\t'*level + str(node.value))
            self._printTree(node.left,level+1)

btree=Tree()
btree.insert(5)
btree.insert(3)
btree.insert(1)
btree.insert(7)
btree.insert(8)
btree.insert(6)
btree.printTree()
