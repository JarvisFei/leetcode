class Node:
    def __init__(self, val):
        self.val = val
        self.next = None








def deleteNode(root, target):

    if not root or not target:
        return "Error"

    if target.next:
        print(target.val)
        target.val = target.next.val
        target.next = target.next.next

    if not target.next:
        while root and root.next:
            if not root.next.next:
                root.next = None
            root = root.next







def main():
    root = Node(10)
    point = root



    for i in range(10):
        point.next = Node(i)
        point = point.next
        target = point


    deleteNode(root,target)


    while root:
        print(root.val)
        root = root.next



if __name__ == "__main__":
    main()



