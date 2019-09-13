class TreeNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None



def getDepth(root):

    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return max([getDepth(root.left), getDepth(root.right)]) + 1

from collections import deque
def getDepth1(root):

    if not root:
        return 0

    queue = deque()
    queue.appendleft((1,root))

    maxdepth = 0
    while queue:
        depth, root = queue.popleft()
        maxdepth = max([maxdepth,depth])
        if root.left:
            queue.append((depth + 1, root.left))
        if root.right:
            queue.append((depth + 1, root.right))

    return maxdepth


def buildBinaryTree(preOrder, midOrder):

    if len(preOrder) == 0 or len(midOrder) == 0 or len(preOrder) != len(midOrder):
        return None

    if len(preOrder) == 1 and len(midOrder) == 1:
        return TreeNode(preOrder[0])

    midIndex = midOrder.index(preOrder[0])

    root = TreeNode(preOrder[0])
    root.left = buildBinaryTree(preOrder[1:midIndex + 1], midOrder[:midIndex])
    root.right = buildBinaryTree(preOrder[midIndex + 1:], midOrder[midIndex + 1:])
    return root



def prinBinaryTree(root):

    if not root:
        return

    print(root.value)

    prinBinaryTree(root.left)
    prinBinaryTree(root.right)


def main():

    preOrder = [1,2,4,5,7,3,6]
    midOrder = [4,2,7,5,1,3,6]

    root = buildBinaryTree(preOrder, midOrder)

    #prinBinaryTree(root)
    result = getDepth1(root)
    print(result)



if __name__ == "__main__":
    main()