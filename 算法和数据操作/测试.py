"""
实现堆排序,问问从大到小还是从小到大
"""

def big_endian(array, start, end):



    while True:

        child = start * 2 + 1
        if child > end:
            break
        if child + 1 <= end and array[child + 1] > array[child]:
            child += 1

        if array[child] > array[start]:
            array[child], array[start] = array[start], array[child]
            start = child
        else:
            break


def heap_sort(array):

    start_node = len(array) // 2 - 1


    #构建大根堆，
    for start in range(start_node, -1, -1):
        big_endian(array, start, len(array) - 1)

    #堆排序，从小到大
    for end in range(len(array) - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        big_endian(array, 0 , end - 1)




#主程序入口
def main():
    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(l)
    heap_sort(l)
    print(l)



if __name__ =="__main__":
    main()
