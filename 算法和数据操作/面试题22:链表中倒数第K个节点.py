class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def DeleteK(root, k):

    #没有删成功
    if not root:
        return False

    count = 0

    parent = root
    point = root

    while point:
        if count > k:
            parent = parent.next
        point = point.next
        count += 1

    if count + 1 < k:
        return False
    if count + 1 == k:
        root = root.next
        return True


    if parent.next.next:
        parent.next = parent.next.next
        return True
    else:
        parent.next = None
        return True





def main():
    root = Node(10)
    point = root
    for i in range(10):
        point.next = Node(i)
        point = point.next

    DeleteK(root, 2)

    while root:
        print(root.val)
        root = root.next





if __name__ == "__main__":
    main()