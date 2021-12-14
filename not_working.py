import random

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
        
    def insert(self, newKey, currNode):
        if currNode.key > newKey:
            if currNode.left is None:
                currNode.left = self.Node(newKey, currNode)
                self._incSize(currNode.left)
                self._balance(currNode)
            else:
                self.insert(newKey, currNode.left)

        elif currNode.key < newKey:
            if currNode.right is None:
                currNode.right = self.Node(newKey, currNode)
                self._incSize(currNode.right)
                self._balance(currNode)
            else:
                self.insert(newKey, currNode.right)

    def _calcSize(self, node):
        if node is None:
            return 0
        
        counter = 0
        counter += self._calcSize(node.left)
        counter += self._calcSize(node.right)
        node.size = counter + 1
        return node.size

    def _incSize(self, node):
        if node.parent is None:
            return
        
        node.parent.size += 1
        self._incSize(node.parent)

    def _balance(self, currNode):
        if currNode.parent is None:
            return

        cSize = currNode.size * self.c
        lSize = 0 if currNode.left is None else currNode.left.size
        rSize = 0 if currNode.right is None else currNode.right.size
        
        if lSize > cSize:
            self._rotateRight(currNode)
            self._calcSize(self.root)
        if rSize > cSize:
            self._rotateLeft(currNode)
            self._calcSize(self.root)
        
        self._balance(currNode.parent)

    # x.right != None is a requirement
    def _rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            y.left = x
            x.parent = y

    # x.left != None is a requirement
    def _rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
            y.right = x
            x.parent = y

    # def _rotateLeft(self, newKey, currNode):
    #     newNode = self.Node(newKey, currNode.parent)
    #     if currNode.parent is not None:
    #         if currNode.parent.left.key == currNode.key:
    #             currNode.parent.left = newNode
    #         else:
    #             currNode.parent.right = newNode
    #     currNode.parent = newNode
    #     newNode.left = currNode.left
    #     newNode.left.parent = newNode
    #     newNode.right = currNode

    # def _rotateRight(self, newKey, currNode):
    #     newNode = self.Node(newKey, currNode.parent)
    #     if currNode.parent is not None:
    #         if currNode.parent.left.key == currNode.key:
    #             currNode.parent.left = newNode
    #         else:
    #             currNode.parent.right = newNode
    #     currNode.parent = newNode
    #     newNode.right = currNode.right
    #     newNode.right.parent = newNode
    #     newNode.left = currNode

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

    class Node:
        def __init__(self, key, parent):
            self.key    = key
            self.parent = parent
            self.left   = None
            self.right  = None
            self.size   = 1

#
# keysToSort = CreateData()
keysToSort = [0, 10, 20, 30, 40, 50, 60 , 70, 80, 90, 100]
tree = BST(keysToSort, 0.51)
print("Input array: ", keysToSort, end='')
tree.printTree()
