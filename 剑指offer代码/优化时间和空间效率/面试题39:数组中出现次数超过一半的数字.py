


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


def quikSort(array, start, end):
    if start == end:
        return
    index = partition(array, start, end)
    quikSort(array,start,index)
    quikSort(array,index + 1,end)



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


def heapSort(array):

    start = (len(array) - 1)//2

    for i in range(start, -1, -1):
        buildHeap(array, i, len(array) - 1)

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        buildHeap(array, 0, i - 1)


def merge(array1, array2):

    if not array1:
        return array2
    if not array2:
        return array1

    result = []

    while array1 or array2:

        if not array1:
            result += array2
            break
        if not array2:
            result += array1
            break

        if array1[0] <= array2[0]:
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))
    return result



def mergeSort(array):

    if len(array) == 1:
        return array

    halfindex = len(array)//2

    left = mergeSort(array[:halfindex])
    right = mergeSort(array[halfindex:])

    return merge(left,right)




"""
第一种办法，就是利用partition函数，找到第K大的数
"""

def moreThanHalfNum1(array, k):

    start = 0
    end = len(array) - 1

    while start < end:
        index = partition(array, start, end)
        if index == k:
            return array[k]
        if index > k:
            end = k
        if index < k:
            start = k



"""
第二种办法，就是利用那个特殊数字出现的次数一定大于其他所有数的次数，
"""
def moreThanHalfNum2(array):

    num = array[0]
    times = 0

    for i in array:
        if i == num:
            times += 1
        else:
            if times > 0:
                times -= 1
            else:
                num = i
    return num


def main():

    test_array = [1,2,3,2,2,2,5,4,2]

    # quikSort(test_array, 0, len(test_array) - 1)
    # heapSort(test_array)

    # print(mergeSort(test_array))

    # print(merge([1,2,3],[2,3,4]))
    # print(test_array)
    # print(test_array[len(test_array)//2])

    # print(moreThanHalfNum1(test_array, 4))
    print(moreThanHalfNum2(test_array))



if __name__ == "__main__":
    main()

