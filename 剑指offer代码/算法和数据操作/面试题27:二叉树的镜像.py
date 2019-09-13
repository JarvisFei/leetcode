class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def imageBTree(root):

    if not root:
        return root

    root.left, root.right = root.right, root.left

    imageBTree(root.left)
    imageBTree(root.right)

    return root


def buildBTree(preOrder, midOrder):

    if len(preOrder) == 0 or len(midOrder) == 0:
        return None

    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])

    rootIndex = midOrder.index(preOrder[0])

    root = TreeNode(preOrder[0])
    root.left = buildBTree(preOrder[1: rootIndex + 1], midOrder[0:rootIndex])
    root.right = buildBTree(preOrder[rootIndex + 1:], midOrder[rootIndex + 1:])
    return root


def printBTree(root):
    if not root:
        return
    print(root.val)
    printBTree(root.left)
    printBTree(root.right)



def main():

    preOrder = [1,2,4,5,3]
    midOrder = [4,2,5,1,3]
    root = buildBTree(preOrder, midOrder)

    printBTree(root)
    result = imageBTree(root)
    printBTree(result)



if __name__ == "__main__":
    main()

