from collections import deque

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




def printBinaryTree(root):

    if not root:
        return root

    queue = deque()


    queue.append((root, 0))
    curdepth = 0
    printTemp = []
    while queue:
        point, depth = queue.popleft()

        if depth > curdepth:
            print(printTemp[::-1])
            curdepth = depth
            printTemp = []

        printTemp.append(point.val)
        #print(point.val, end=" ")


        if point.left:
            queue.append((point.left,depth + 1))
        if point.right:
            queue.append((point.right,depth + 1))
    print(printTemp)




def buildBinaryTree(preOrder, midOrder):

    if len(preOrder) == 0 or len(midOrder) == 0:
        return None

    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])

    indexofroot = midOrder.index(preOrder[0])

    root = TreeNode(preOrder[0])

    root.left = buildBinaryTree(preOrder[1: indexofroot+1], midOrder[:indexofroot])
    root.right = buildBinaryTree(preOrder[indexofroot+1:], midOrder[indexofroot+1:])
    return root



def main():

    preOrder = [8,6,5,7,10,9,11]
    midOrder = [5,6,7,8,9,10,11]

    # preOrder = [1,2,3,4,5,6,7]
    # midOrder = [7,6,5,4,3,2,1]
    root = buildBinaryTree(preOrder, midOrder)

    printBinaryTree(root)

"""
这一个题目的变体，是，打印分行的、打印不分行的、打印之字型的
"""

if __name__ == "__main__":
    main()