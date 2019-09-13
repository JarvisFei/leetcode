
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getTopK(root, K):

    if not root:
        return

    stack = []
    result = []

    while stack or root:

        while root:
            stack.append(root)
            root = root.left

        if stack:
            root = stack.pop()
            result.append(root.val)
            root = root.right

    if K > len(result):
        return None

    return result[-K]







def buildBinaryTree(preOrder, midOrder):

    if len(preOrder) == 0 or len(midOrder) == 0:
        return None

    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])

    midIndex = midOrder.index(preOrder[0])

    root = TreeNode(preOrder[0])

    root.left = buildBinaryTree(preOrder[1:midIndex + 1], midOrder[:midIndex])
    root.right = buildBinaryTree(preOrder[midIndex + 1:], midOrder[midIndex + 1:])

    return root

def printBinaryTree(root):

    if not root:
        return

    print(root.val)
    printBinaryTree(root.left)
    printBinaryTree(root.right)



def main():
    preOrder = [5,3,2,4,7,6,8]
    midOrder = [2,3,4,5,6,7,8]

    root = buildBinaryTree(preOrder, midOrder)

    #printBinaryTree(root)
    result = getTopK(root,3)
    print(result)



if __name__ == "__main__":
    main()