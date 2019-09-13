class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def judgeTree(Tree1, Tree2):

    #假定空树是任意树的子树
    if not Tree1 and not Tree2:
        return True

    if not Tree1 or not Tree2:
        return False

    if Tree1.val == Tree2.val:
        if judgeTree(Tree1.left, Tree2.left) and judgeTree(Tree1.right, Tree2.right):
            return True
    else:
        if judgeTree(Tree1.left, Tree2) or judgeTree(Tree1.right, Tree2):
            return True
    return False




def buildTree(preOrder, midOrder):

    if not preOrder or not midOrder:
        return None

    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])


    rootIndex = midOrder.index(preOrder[0])

    result = TreeNode(preOrder[0])
    result.left = buildTree(preOrder[1:rootIndex+1], midOrder[0:rootIndex])
    result.right = buildTree(preOrder[rootIndex+1:], midOrder[rootIndex+1:])
    return result

def printTree(root):

    if not root:
        return None

    print(root.val)
    printTree(root.left)
    printTree(root.right)


def main():
    preOrder = [1,2,4,5,3]
    midOrder = [4,2,5,1,3]
    Tree1 = buildTree(preOrder, midOrder)

    preOrder = [2, 4, 5]
    midOrder = [4, 2, 5]
    Tree2 = buildTree(preOrder, midOrder)

    result = judgeTree(Tree1, Tree2)
    print(result)




if __name__ == "__main__":
    main()
