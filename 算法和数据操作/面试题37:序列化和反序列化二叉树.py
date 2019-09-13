class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def buildBinaryTree(preOrder, midOrder):
    if len(preOrder) == 0 or len(midOrder) == 0:
        return
    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])

    rootIndex = midOrder.index(preOrder[0])
    root = TreeNode(preOrder[0])
    root.left = buildBinaryTree(preOrder[1:rootIndex+1], midOrder[0:rootIndex])
    root.right = buildBinaryTree(preOrder[rootIndex+1:],midOrder[rootIndex+1:])

    return root


def printBinaryTree(root):

    if not root:
        return

    print(root.val)
    printBinaryTree(root.left)
    printBinaryTree(root.right)


def serialize(root):

    result = ""

    if not root:
        result += "$"
        return result

    return str(root.val) +","+ serialize(root.left) +","+ serialize(root.right)


def deserialize(array):

    if not array:
        return None

    val = array.pop(0)
    root = None
    if val != "$":
        root = TreeNode(val)
        root.left = deserialize(array)
        root.right = deserialize(array)
    return root






def main():
    preOrder = [1,2,4,3,5,6]
    midOrder = [4,2,1,5,3,6]
    root = buildBinaryTree(preOrder, midOrder)
    # printBinaryTree(root)

    result = serialize(root)
    print(result)
    result = deserialize(result.split(","))
    printBinaryTree(result)






if __name__ == "__main__":
    main()