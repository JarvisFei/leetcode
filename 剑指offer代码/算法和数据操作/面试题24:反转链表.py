class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def reverse(root):
    point = root
    parent = None

    while point:

        point.next, point, parent = parent, point.next,point
        if not point:
            return parent




def main():

    root = Node(10)
    point  = root
    for i in range(10):
        point.next = Node(i)
        point = point.next

    result = reverse(root)
    while result:
        print(result.val)
        result = result.next




if __name__ == "__main__":
    main()