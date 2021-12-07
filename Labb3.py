class BST:
    def __init__(self, keys):
        self.root = self.Node(keys[0], None)
        for i in range(1, len(keys)):
            self.insert(keys[i], self.root)

    def insert(self, newKey, currNode):
        if currNode.key > newKey:
            if currNode.left is None:
                currNode.left = self.Node(newKey, currNode)
            else:
                self.insert(newKey, currNode.left)
        elif currNode.key < newKey:
            if currNode.right is None:
                currNode.right = self.Node(newKey, currNode)
            else:
                self.insert(newKey, currNode.right)

    def balanceBST(self):
        return -1
        #code

    # NOT TESTED!
    def printTree(self, currNode = -1):
        if currNode is None:
            return 0

        if currNode == -1:
            currNode = self.root
            print("\nThe current tree:\n")
        
        # Check for None!!!!!!!
        print(currNode.key, "\n", currNode.left.key, currNode.right.key)
        self.printTree(currNode.left)
        self.printTree(currNode.right)

    class Node:
        def __init__(self, key, parent, left = None, right = None):
            self.key    = key
            self.parent = parent
            self.left   = left
            self.right  = right
            #self.size   = self.calcSize()

        def calcSize(self):
            return 0

keysToSort = [10, 5, 15, 0, 20]
tree = BST(keysToSort)
tree.printTree()
