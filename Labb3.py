class BST:
    def __init__(self, keys, c):
        self.c    = c
        self.root = self.Node(keys[0], None)
        for i in range(1, len(keys)):
            self.insert(keys[i], self.root)

        # Calc size for every node
        self.root.calcSize(self.root)

    def insert(self, newKey, currNode):
        newLeafNode = self._createLeaf(newKey, currNode)
        if newLeafNode is None:
            return

        #self._balanceBST(newLeafNode)

    def _balanceBST(self, node):
        parentSize = node.parent.left.size + node.parent.right.size
        if (node.parent.left.size * self.c > parentSize or
            node.parent.right.size * self.c > parentSize):
            #Code

            return

        self._balanceBST(node.parent)

    def _createLeaf(self, newKey, currNode):
        if currNode.key > newKey:
            if currNode.left is None:
                currNode.left = self.Node(newKey, currNode)
                return currNode.left
            else:
                self._createLeaf(newKey, currNode.left)

        elif currNode.key < newKey:
            if currNode.right is None:
                currNode.right = self.Node(newKey, currNode)
                return currNode.right
            else:
                self._createLeaf(newKey, currNode.right)

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

        def calcSize(self, node):
            if node is None:
                return 0
            
            counter = 0
            counter += self.calcSize(node.left)
            counter += self.calcSize(node.right)
            node.size = counter + 1
            return node.size

keysToSort = [10, 5, 15, 0, 20]
tree = BST(keysToSort, 0.5)
print("Input array: ", keysToSort, end='')
tree.printTree()
