class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




def buildBinaryTree(preOrder, midOrder):

    if len(preOrder) == 0 and len(midOrder) == 0:
        return None

    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])

    rootIndex = midOrder.index(preOrder[0])

    root = TreeNode(preOrder[0])
    root.left = buildBinaryTree(preOrder[1:rootIndex + 1], midOrder[0:rootIndex])
    root.right = buildBinaryTree(preOrder[rootIndex + 1:], midOrder[rootIndex + 1:])

    return root


def printBinaryTree(root):

    if not root:
        return

    print(root.val)
    printBinaryTree(root.left)
    printBinaryTree(root.right)

def imageBinaryTree(root):

    if not root:
        return root

    result = TreeNode(root.val)
    result.left = imageBinaryTree(root.right)
    result.right = imageBinaryTree(root.left)
    return result


def judgeBinaryTree(root,imageRoot):
    if not root and not imageRoot:
        return True

    if root.val == imageRoot.val:
        return judgeBinaryTree(root.left,imageRoot.left) and judgeBinaryTree(root.right,imageRoot.right)
    else:
        return False




def main():
    preOrder = [8,6,5,7,6,7,5]
    midOrder = [5,6,7,8,7,6,5]

    root = buildBinaryTree(preOrder,midOrder)
    printBinaryTree(root)

    printBinaryTree(imageBinaryTree(root))

    result = judgeBinaryTree(root, imageBinaryTree(root))
    print(result)



if __name__ == "__main__":
    main()