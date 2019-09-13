class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def buildBinaryTree(preOrder, midOrder):

    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])

    rootIndex = midOrder.index(preOrder[0])
    root = TreeNode(preOrder[0])

    root.left = buildBinaryTree(preOrder[1:rootIndex+1],midOrder[0:rootIndex])
    root.right = buildBinaryTree(preOrder[rootIndex+1:],midOrder[rootIndex+1:])

    return root

def printBinaryTree(root):

    if not root:
        return

    print(root.val)
    printBinaryTree(root.left)
    printBinaryTree(root.right)


def convertBinaryTree(root):


    if not root:
        return None
    if not root.left and not root.right:
        return root

    left = convertBinaryTree(root.left)

    point = left

    while point.right:
        point = point.right
    right = convertBinaryTree(root.right)

    point.right = root
    root.left = point
    root.right = right
    right.left = root

    return left



def main():
    preOrder = [10,6,4,8,14,12,16]
    midOrder = [4,6,8,10,12,14,16]

    root = buildBinaryTree(preOrder, midOrder)
    printBinaryTree(root)
    result = convertBinaryTree(root)

    while result:
        print(result.val, end=" ")
        result = result.right




if __name__ == "__main__":
    main()