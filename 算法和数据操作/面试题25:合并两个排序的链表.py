class Node():
    def __init__(self, val):

        self.val = val
        self.next = None


def merge(link1, link2):

    if not link1:
        return link2
    if not link2:
        return link1


    result = Node(0)
    root = result
    point1 = link1
    point2 = link2

    while point1 and point2:

        if point1.val <= point2.val:
            root.next = point1
            root = root.next
            point1 = point1.next
        else:
            root.next = point2
            root = root.next
            point2 = point2.next

    if point1  and not point2:
        root.next = point1
    if point2 and not point1:
        root.next = point2

    return result.next


def main():
    root1 = Node(1)
    point = root1
    for i in range(2,9):
        point.next = Node(i)
        point = point.next

    root2 = Node(4)
    point = root2
    for i in range(5,15):
        point.next = Node(i)
        point = point.next


    result = merge(root1, root2)
    while result:
        print(result.val)
        result = result.next



if __name__ == "__main__":
    main()