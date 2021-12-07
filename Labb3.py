class BST:
    def __init__(self, keys):
        self.root = self.Node(keys[0], None)
        for i in range(1, len(keys)):
            self.insert(keys[i], self.root)
        # Calc size for every node        

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
        def __init__(self, key, parent, left = None, right = None):
            self.key    = key
            self.parent = parent
            self.left   = left
            self.right  = right
            self.size   = self.calcSize(self)

        # NEEDS FURTHER TESTING
        def calcSize(self, node):
            counter = 0
        
            if node is None:
                return 0

            counter += self.calcSize(node.left)
            counter += self.calcSize(node.right)

            return counter + 1

keysToSort = [10, 5, 15, 0, 20]
tree = BST(keysToSort)
tree.printTree()
