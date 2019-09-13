class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


preOrder = [1,2,4,7,3,5,6,8]
midOrder = [4,7,2,1,5,3,8,6]


def BuildTree(preOrder,midOrder):

    if len(preOrder) != len(midOrder) or len(preOrder) == 0:
        return

    if len(preOrder) == len(midOrder) and len(preOrder) == 1:
        return TreeNode(preOrder[0])

    midIndex = midOrder.index(preOrder[0])

    left = BuildTree(preOrder[1 : midIndex + 1],midOrder[0:midIndex])
    right = BuildTree(preOrder[midIndex + 1:], midOrder[midIndex + 1:])

    root = TreeNode(preOrder[0])
    root.left = left
    root.right = right
    return root



root = BuildTree(preOrder, midOrder)


result = []
def DFS(root):
    if not root:
        return
    result.append(root.val)
    DFS(root.left)
    DFS(root.right)

DFS(root)
print(result)


#这里写一点中序遍历的代码

def midOrder(root,target):
    if not root:
        return

    stack = []
    res = []
    flag = False

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            res.append(root.val)
            if flag:
                print(root.val)
                flag = False
            if root.val == target:
                flag = True
            root = root.right
    print(res)
midOrder(root,4)