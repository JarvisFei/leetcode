class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def getCom(Link1, Link2):

    visited = set()

    while Link1:
        visited.add(Link1)
        Link1 = Link1.next

    while Link2:
        if Link2 in visited:
            return Link2
        Link2 = Link2.next

    return None



def main():

    Link1 = Node(0)
    Link2 = Node(0)
    point1 = Link1
    point2 = Link2

    for i in range(1,50):
        if i < 10:
            point1.next = Node(i)
            point1 = point1.next

        elif i >= 10 and i < 20:
            point2.next = Node(i)
            point2 = point2.next

        else:
            point1.next = point2.next = Node(i)
            point1 = point1.next
            point2 = point2.next


    result = getCom(Link1, Link2)
    print(result.val)


if __name__ == "__main__":
    main()