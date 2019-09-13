class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def findRecNode(root):

    if not root:
        return root
    point = root

    count = set()

    while point:
        if point.val not in count:
            count.add(point.val)
            point = point.next
        else:
            return point




def main():
    root = Node(10)
    point = root

    targetNode = None

    for i in range(10):
        point.next = Node(i)
        point = point.next

        if i == 3:
            targetNode = point
        if i == 9:
            point.next = targetNode

    result = findRecNode(root)
    print(result.val)
    # while root:
    #     print(root.val)
    #     root = root.next


if __name__ == "__main__":
    main()