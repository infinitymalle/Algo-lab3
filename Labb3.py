import random
import cProfile

def CreateData():
    dataset = []

    for i in range(1000):
        #dataset.append(random.randrange(0, 1001))
        dataset.append(i)                          # fills the dataset with already sorted data
        # Creates an almost sorted dataset, every tenth loop the input will be randomized
        #if i % 10 == 0: dataset.append(random.randrange(0, 101))
        #else: dataset.append(i)
    #print("test", dataset)
    return dataset

class BST:
    def __init__(self, root, c):
        self.c    = c
        self.root = self.Node(root, None)

        #self.root = self._buildTree(keys, 0, len(keys)-1)
        #self._calcSize(self.root)

        #self.root = self.Node(keys[0], None)
        #testInserts = [11, 12, 13, 14, 15]
        
    def insert(self, newKey, currNode = None):
        if currNode is None:
            currNode = self.root

        if currNode.key >= newKey:                          # Kollar om nya värdet ska till höger eller vänster om currentnode
            if currNode.left is None:                       # Kollar om noden är ledig 
                currNode.left = self.Node(newKey, currNode) # Lägger in en ny nod
                self._incSize(currNode.left)                # Ökar noderna size på alla noder längs sökvägens med 1
                self._balance(currNode)                     # Kollar om det behöver balanseras längs sökvägen
            else:
                self.insert(newKey, currNode.left)          # Om noden var upptagen anropar igen en ner

        elif currNode.key < newKey:
            if currNode.right is None:
                currNode.right = self.Node(newKey, currNode)
                self._incSize(currNode.right)
                self._balance(currNode)
            else:
                self.insert(newKey, currNode.right)

    def _buildTree(self, sortedList, left_i, right_i, parent = None):   # bygger om trädet från noden till ett prefekt balanserat träd
        if left_i > right_i:                                            # Listan måste vara sorterad
            return None

        mid_i = (left_i + right_i) // 2
        root = self.Node(sortedList[mid_i], parent)
        root.left = self._buildTree(sortedList, left_i, mid_i-1, root)
        root.right = self._buildTree(sortedList, mid_i+1, right_i, root)
        return root

    def _calcSize(self, node):                  # Beräknar storleken på noden
        if node is None:
            return 0
        
        counter = 0
        counter += self._calcSize(node.left)
        counter += self._calcSize(node.right)
        node.size = counter + 1
        return node.size

    def _incSize(self, node):                   # Ökar noderna size på alla noder längs sökvägens med 1
        if node.parent is None:
            return
        
        node.parent.size += 1
        self._incSize(node.parent)

# Check balance of given (sub)tree with respect to c, uses a bottom-up approach
    def _balance(self, currNode):     
        # When tree root has been reached          
        if currNode is None:
            return
        #currNode = local root
        cSize = currNode.size * self.c
        lSize = 0 if currNode.left is None else currNode.left.size
        rSize = 0 if currNode.right is None else currNode.right.size
        
        # Check if re-balancing is needed
        if lSize > cSize or rSize > cSize:
            # Create new perfect balanced BST
            sortedList = self._bSort(self._depthSearch(currNode))
            balanced_tree = self._buildTree(sortedList, 0, len(sortedList)-1, currNode.parent)
            self._calcSize(balanced_tree)

            # Replace existing (sub)tree with new tree
            if currNode.parent is None:
                self.root = balanced_tree

            elif currNode.parent.left is not None:
                if currNode.parent.left.key == currNode.key:
                    currNode.parent.left = balanced_tree
            elif currNode.parent.right is not None:
                if currNode.parent.right.key == currNode.key:
                    currNode.parent.right = balanced_tree

        self._balance(currNode.parent)

    def _depthSearch(self, currNode):                           # Retunerar en lista med alla keys från en viss nod och under den
        if (currNode.left is None and currNode.right is None):  # Kollar om den nått ett löv
            return [currNode.key]

        left  = []
        right = []
        if (currNode.left != None):                             # Kollar om något är i lövet 
            left = self._depthSearch(currNode.left)

        if (currNode.right != None):
            right = self._depthSearch(currNode.right)

        return left + [currNode.key] + right                    # Allt som är till vänster om noden + noden själv + allt till höger

    # Assumes sorted list of integers
    def _binSrc(self, query, list, L_i, R_i):
        # Initial checks: Checks for empty lists and if query is within list range
        if query > list[0] and len(list) == 1:
            return 1
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

#    def _printInorder(self, root, lst):
# 
#        if (root != None):
#            self._printInorder(root.left, lst)
#    
#            # then print the data of node
#            lst.append(root.key)
#    
#            # now recur on right child
#            self._printInorder(root.right, lst)
#        return(lst)
#
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



#keysToSort = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
def test(keys, rootkey, c):
    tree = BST(rootkey, c)
    #print("Input array: ", keys, end='')
    for i in range(len(keys)):
        tree.insert(keys[i], tree.root)
    #tree.printTree()

keys = CreateData()
rootkey = keys[0]
keys.pop(0)

#cProfile.run('test(keys, rootkey, 0.51)')      #tester
#cProfile.run('test(keys, rootkey, 0.6)')
#cProfile.run('test(keys, rootkey, 0.7)')
#cProfile.run('test(keys, rootkey, 0.8)')
#cProfile.run('test(keys, rootkey, 0.9)')
cProfile.run('test(keys, rootkey, 0.99)')
