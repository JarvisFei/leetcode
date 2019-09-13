
"""
这个问题是，TopK算法的同类问题
解决方法有两种：
1,使用块排的partition函数
2,使用堆排序
"""

def partition(array, start, end):

    base = array[start]

    while start <= end:

        if start == end:
            array[start] = base
            return start

        while start < end and array[end] >= base:
            end -= 1
        array[start] = array[end]
        while start < end and array[start] < base:
            start += 1
        array[end] = array[start]

"""
一定要注意，partition的函数，返回的是左边小，右边大，所以，返回的index值，要有所变化
"""

def topK_quikSort(array, k):

    if len(array) <= k:
        return array

    if len(array) == 0:
        return 0

    start = 0
    end = len(array) - 1

    while start <= end:

        index = partition(array, start, end)

        if index == k:
            return array[:k]

        if index > k:
            end = index - 1
        else:
            start = index + 1


"""
下面开始堆排序
"""

def buildHeap(array, start, end):

    while start <= end:
        child = start * 2 + 1

        if child + 1 <= end and array[child + 1] > array[child]:
            child += 1

        if child <= end and array[child] > array[start]:
            array[child], array[start] = array[start], array[child]
            start = child
        else:
            break

def topK_heapSort(arrary, k):

    if len(arrary) <= k:
        return arrary

    if len(arrary) == 0:
        return None

    result = arrary[:k]

    start = (len(result) - 1)//2

    for i in range(start, -1, -1):
        buildHeap(result, i, len(result) - 1)
    print(result)
    for i in arrary[k:]:
        if i < result[0]:
            result[0] = i
            buildHeap(result,0, len(result) - 1)

    return result




def main():

    test_array = [4,5,1,6,2,7,3,8]
    result = topK_heapSort(test_array, 5)
    print(result)



if __name__ == "__main__":
    main()