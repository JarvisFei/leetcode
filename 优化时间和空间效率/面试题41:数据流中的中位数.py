
def buildbigheap(array, start, end):

    while start <= end:

        child = start * 2 + 1

        if child + 1 <= end and array[child + 1] > array[child]:
            child += 1

        if child <= end and array[child] > array[start]:
            array[child], array[start] = array[start], array[child]
            start = child
        else:
            break

def buildsmallheap(array, start, end):

    while start <= end:
        child = start * 2 +1

        if child + 1 <= end and array[child + 1] < array[child]:
            child += 1

        if child <= end and array[child] < array[start]:
            array[start], array[child] = array[child], array[start]
            start = child
        else:
            break


def insertbigheap(arrary, num = None):

    if num:
        arrary.append(num)

    start = (len(arrary) -  1)//2

    for i in range(start, -1, -1):
        buildbigheap(arrary, i, len(arrary) - 1)

def insertsmallheap(arrary, num = None):

    if num:
        arrary.append(num)

    start = (len(arrary) - 1)//2

    for i in range(start, -1, -1):
        buildsmallheap(arrary, i, len(arrary) - 1)


def getMedian(array):

    big = []
    small = []

    for i in range(len(array)):
        if i % 2 == 0:
            if big and array[i] < big[0]:
                array[i],big[0] = big[0], array[i]
                insertbigheap(big)
            insertsmallheap(small, array[i])
        else:
            if small and array[i] > small[0]:
                array[i], small[0] = small[0], array[i]
                insertsmallheap(small)
            insertbigheap(big, array[i])

    if len(array) % 2 == 0:
        print(big,small)
        return (big[0] + small[0]) / 2
    else:
        print(big, small)
        return small[0]


def main():
    test_array = [1,2,3,4,5,6,7,8,9,10]
    result = getMedian(test_array)
    print(result)


if __name__ == "__main__":
    main()