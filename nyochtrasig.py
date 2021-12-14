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
    # keys needs to be sorted
    def __init__(self, keys, c):
        self.c    = c
        self.root = self._buildTree(keys, 0, len(keys)-1)
        self._calcSize(self.root)

        #self.root = self.Node(keys[0], None)
        testInserts = [11, 12, 13, 14, 15]
        for i in range(1, len(testInserts)):
            self.insert(testInserts[i], self.root)
        
    def insert(self, newKey, currNode = None):
        if currNode is None:
            currNode = self.root

        if currNode.key > newKey:
            if currNode.left is None:
                currNode.left = self.Node(newKey, currNode)
                self._incSize(currNode.left)
                currNode.parent.parent.left = self._balance(currNode)
            else:
                self.insert(newKey, currNode.left)

        elif currNode.key < newKey:
            if currNode.right is None:
                currNode.right = self.Node(newKey, currNode)
                self._incSize(currNode.right)
                currNode.parent.parent.right = self._balance(currNode) # här går det fel när inget behöver balanseras
                print("test")
            else:
                self.insert(newKey, currNode.right)

    def _buildTree(self, sortedList, left_i, right_i, parent = None):
        if left_i > right_i:
            return None

        mid_i = (left_i + right_i) // 2
        root = self.Node(sortedList[mid_i], parent)
        root.left = self._buildTree(sortedList, left_i, mid_i-1, root)
        root.right = self._buildTree(sortedList, mid_i+1, right_i, root)
        return root

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
        if currNode is None:
            return

        cSize = currNode.size * self.c
        lSize = 0 if currNode.left is None else currNode.left.size
        rSize = 0 if currNode.right is None else currNode.right.size
        
        if lSize > cSize or rSize > cSize:
            #sortedList = self._bSort(self._depthSearch(currNode))
            sortedList = self._depthSearch(currNode)
            sortedList.sort()            
            currNode = self._buildTree(sortedList, 0, len(sortedList)-1, currNode.parent)
            self._calcSize(currNode)
            return currNode
        
        if currNode.parent is not None:
            currNode = self._balance(currNode.parent)
            return currNode
        else:
            return currNode

    def _depthSearch(self, currNode):
        if (currNode.left is None and currNode.right is None):
            return [currNode.key]

        left  = []
        right = []
        if (currNode.left != None):
            left = self._depthSearch(currNode.left)

        if (currNode.right != None):
            right = self._depthSearch(currNode.right)

        return left + [currNode.key] + right

    # Assumes sorted list of integers
    def _binSrc(self, query, list, L_i, R_i):
        # Initial checks: Checks for empty lists and if query is within list range
        if R_i < 1:
            return -1
        if query < list[0]:
            return 0
        if query > list[R_i]:
            return R_i + 1

        middle_i = (L_i + R_i) // 2

        # Base case
        if list[middle_i] == query or R_i - L_i == 1:
            return middle_i + 1

        elif list[middle_i] > query:
            return self._binSrc(query, list, L_i, middle_i)

        else:
            return self._binSrc(query, list, middle_i, R_i)

    def _bSort(self, list):
        if len(list) < 2:
            return list

        sortedList = [list[0]]
        for i in range(1, len(list)):
            index = self._binSrc(list[i], sortedList, 0, len(sortedList)-1)
            sortedList.insert(index, list[i])

        return sortedList

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

#keysToSort = CreateData()
keysToSort = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = BST(keysToSort, 0.51)
print("Input array: ", keysToSort, end='')
tree.printTree()