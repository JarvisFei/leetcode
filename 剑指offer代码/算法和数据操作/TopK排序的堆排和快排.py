"""
堆排的时间复杂度是nlog(K)
快排的时间复杂度是n
但是快排的话，需要将所有的数都读到内存里面，而堆排只需要维护长度为K的数组就可以
"""



def BuildHeap(array, start, end):

    while True:

        child = start * 2 + 1
        if child > end:
            return
        if child + 1 <= end and array[child + 1] > array[child]:
            child += 1
        if array[child] > array[start]:
            array[child], array[start] = array[start], array[child]
            start = child
        else:
            return




def HeapSort(array, k):

    if len(array) <= k :
        return array

    result = array[:k]

    for i in range(int(len(result)/2 - 1), -1, -1):
        BuildHeap(result,i, len(result) - 1)

    print(result)
    for i in array[k:]:

        if i < result[0]:
            result[0] = i
            BuildHeap(result, 0, len(result) - 1)

    return result




def Partition(array, start, end):

    base = array[start]

    while start <= end:

        if start == end:
            array[start] = base
            return start
        while end > start and array[end] > base:
            end -= 1
        array[start] = array[end]
        while end > start and array[start] < base:
            start += 1
        array[end] = array[start]


def QuikSort(array, k):
    start = 0
    end = len(array) - 1
    while True:
        index = Partition(array,start, end)

        if index == start:
            index += 1
        if index == end:
            index -= 1

        if index == k:
            return array[:k]
        if index > k:
            end = index
        else:
            start = index


def main():

    test = [1,9,6,3,11,3,55,89,0,34,54]

    result = QuikSort(test, 6)
    print(result)

    print(test)



if __name__ == "__main__":
    main()