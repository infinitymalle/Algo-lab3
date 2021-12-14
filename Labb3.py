import random
import math


def CreateData():
    dataset = []

    for i in range(10):
        dataset.append(random.randrange(0, 11))
        #dataset.append(i)                          # fills the dataset with already sorted data
        # Creates an almost sorted dataset, every tenth loop the input will be randomized
        #if i % 10 == 0: dataset.append(random.randrange(0, 101))
        #else: dataset.append(i)
    #print("test", dataset)
    return dataset

class BST:
    def __init__(self, keys, c):
        self.c    = c
        self.root = self.Node(keys[0], None)
        for i in range(1, len(keys)):
            self.insert(keys[i], self.root)

        # Calc size for every node
        self.calcSize(self.root)

    def calcSize(self, node):
        if node is None:
            return 0
        
        counter = 0
        counter += self.calcSize(node.left)
        counter += self.calcSize(node.right)
        node.size = counter + 1
        return node.size
        
    def insert(self, newKey, currNode):
        cSize = currNode.size * self.c
        if currNode.key > newKey and currNode.left.size < cSize:
            if currNode.left is None:
                currNode.left = self.Node(newKey, currNode)
                return currNode.left
            else:
                self.insert(newKey, currNode.left)

        else:
            self._rotateLeft(newKey, currNode)

        if currNode.key < newKey and currNode.right.size < cSize:
            if currNode.right is None:
                currNode.right = self.Node(newKey, currNode)
                return currNode.right
            else:
                self.insert(newKey, currNode.right)

        else:
            self._rotateRight(newKey, currNode)
            
    def _rotateLeft(self, newKey, currNode):
        newNode = self.Node(newKey, currNode.parent)
        if currNode.parent.left.key == currNode.key:
            currNode.parent.left = newNode
        else:
            currNode.parent.right = newNode
        currNode.parent = newNode
        newNode.left = currNode.left
        newNode.left.parent = newNode
        newNode.right = currNode

    def _rotateRight(self, newKey, currNode):
        newNode = self.Node(newKey, currNode.parent)
        if currNode.parent.left.key == currNode.key:
            currNode.parent.left = newNode
        else:
            currNode.parent.right = newNode
        currNode.parent = newNode
        newNode.right = currNode.right
        newNode.right.parent = newNode
        newNode.left = currNode

    def printTree(self, currNode = -1):
        if currNode is None:
            return 0

        if currNode == -1:
            currNode = self.root
            print("\nThe current tree:")
        
        print("")
        print("    ", currNode.key)
        print("  /\t\\")
        print(
            currNode.left.key if currNode.left is not None else "None",
            "\t", currNode.right.key if currNode.right is not None else "None"
        )
        self.printTree(currNode.left)
        self.printTree(currNode.right)
    
    def balance(self, currnode):
        if(currnode.parent == None):
            return(None)
        if (currnode.left > self.c * currnode.size):
            self._rotateLeft(currnode)
        if (currnode.right > self.c * currnode.size):
            self._rotateRight(currnode)
        
        self.balance(currnode.parent)

    def depthSearch(self, currnode):
        if (currnode.left == None and currnode.right == None):
            return([currnode.key])

        
        if (currnode.left != None):
            left = self.depthSearch(currnode.left)
        if (currnode.right != None):
            right = self.depthSearch(currnode.right)
        return(left.append(currnode.key) + right)

    class Node:
        def __init__(self, key, parent):
            self.key    = key
            self.parent = parent
            self.left   = None
            self.right  = None
            self.size   = 1

    

keysToSort = CreateData()
tree = BST(keysToSort, 0.5)
print("Input array: ", keysToSort, end='')
tree.printTree()
