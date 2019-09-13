
"""
测试例子
"""

test = [2,4,5,9,1,4,93,64,23,67,87,55,35,91]
print(test)

"""
1.快速排序算法
"""

#快速排序的简单实现
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])



#快排的递归实现
import numpy as np
def QuikSort(array, l, r):
    if l >= r:
        return
    baseIndex = np.random.randint(l, r)
    base = array[l]
    i = l
    j = r
    while i <= j:
        if i == j:
            array[i] = base
            break
        while i < j and array[j] >= base:
            j -= 1
        array[i] = array[j]
        while i< j and array[i] < base:
            i += 1
        array[j] = array[i]
    QuikSort(array, l, i - 1)
    QuikSort(array, i + 1, r)
#QuikSort(test,0, len(test) - 1)
#print(test)


#快排的简单实现
def QuikSort2(array, l, r):
    if l < r:
        q = partition(array, l, r)
        QuikSort2(array,l, q - 1)
        QuikSort2(array, q + 1, r)

def partition(array, l, r):

    base = array[r]

    q = l - 1

    for i in range(l, r):
        if array[i] < base:
            q += 1
            array[q], array[i] = array[i], array[q]
    array[q + 1], array[r] = array[r], array[q + 1]

    return q + 1

#QuikSort2(test,0, len(test) - 1)
#print(test)




"""
2.归并排序算法
"""


#基于数组的归并排序
def merge(array1, array2):
    result = []

    while array1 or array2:
        if not array1:
            result.extend(array2)
            array2 = []
        elif not array2:
            result.extend(array1)
            array1 = []
        else:
            if array1[0] < array2[0]:
                result.append(array1[0])
                array1 = array1[1:]
            elif array1[0] >= array2[0]:
                result.append(array2[0])
                array2 = array2[1:]
    return result

def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = int(len(array) / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


test = merge_sort(test)


#基于链表的归并排序
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
root = Node(8)
point = root
for i in np.random.randint(0,100,10):
    point.next = Node(i)
    point = point.next


def merge2(linklist1, linklist2):

    if not linklist1 and not linklist2:
        return None
    if not linklist1 and linklist2:
        return linklist2
    if linklist1 and not linklist2:
        return linklist1

    if linklist1.val > linklist2.val:
        res = linklist2
    else:
        res = linklist1

    while linklist2 and linklist1:
        if linklist1.val < linklist2.val:
            linklist1, linklist1.next = linklist1.next, linklist2
        elif linklist2.val <= linklist1.val:
            linklist2, linklist2.next = linklist2.next, linklist1

    return res

def merge3(left, right):
    pre = Node(-1)
    first = pre
    print("")
    while left and right:
        if left.val < right.val:
            pre.next = left
            pre = left
            left = left.next
        else:
            pre.next = right
            pre = right
            right = right.next
    if left:
        pre.next = left
    else:
        pre.next = right

    return first.next


def merge_sort2(linklist):
    if not linklist and not linklist.next:
        return linklist

    mid = linklist
    end = linklist
    pre = linklist

    while end and end.next:
        pre = mid
        mid = mid.next
        end = end.next.next


    sec_linklist = pre.next
    pre.next = None

    left = merge_sort2(linklist)
    right = merge_sort2(sec_linklist)

    return merge2(left, right)

root = merge3(root,root)
while root:
    print(root.val)
    root = root.next







