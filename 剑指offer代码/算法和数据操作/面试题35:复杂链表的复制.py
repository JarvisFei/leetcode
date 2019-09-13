"""
复杂链表的复制，分为三种方法
1.第一步复制链表，第二步复制任意指针的指向，寻找任意指针的指向的方法是从头开始找，O(n2)
2.第一步复制链表，第二步复制任意指针的指向，用hash表存储原始节点和复制节点对,时间复杂度是O(n),但是空间复杂度是O(n)
3.第一步复制链表，第二步复制任意指针的指向，第一步复制的节点，直接插入到原节点后面，这样时间复杂度依然后O(n),但是空间复杂度是O(1)
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.p = None

def copyLink(root):

    result = Node(0)
    point = result

    root1 = root
    while root:
        point.next = Node(root.val)
        point = point.next
        root = root.next


    point = result.next
    # print("1")
    root = root1
    while root:
        if root.p:
            # print("2")
            tempPoint = result.next
            while tempPoint:
                if tempPoint.val == root.p.val:
                    point.p = tempPoint
                    # print(point.p.val,"yin")
                tempPoint = tempPoint.next
        point = point.next
        root = root.next
    return result.next


def copyLink2(root):

    result = Node(0)

    point_root = root
    point_result = result

    node_pair = {}

    while point_root:
        point_result.next = Node(point_root.val)
        point_result = point_result.next
        node_pair[point_root] = point_result
        point_root = point_root.next

    point_root = root
    point_result = result.next
    while point_root:
        if point_root.p:
            point_result.p = node_pair[point_root.p]
        point_root = point_root.next
        point_result = point_result.next


    return result.next



def copyLink3():
    pass


def main():

    root = Node(0)
    point = root

    for i in range(1,11):
        point.next = Node(i)
        if i == 3:
            target1 = point
        if i == 8:
            target2 = point
        point = point.next

    point = root
    while point:
        if point.val == 5:
            point.p = target1
        if point.val == 6:
            point.p = target2

        point = point.next

    result = copyLink2(root)

    while result:
        # print(result.val)
        if result.val == 6:
            print(result.p.val)
        # if result.val == 6:
        #     print(result.p.val)
        result = result.next







if __name__ == "__main__":
    main()
