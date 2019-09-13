
def getTarget(array, target):

    start = 0
    end = len(array) - 1

    while start < end:

        if array[start] + array[end] > target:
            end -= 1
        elif array[start] + array[end] < target:
            start += 1
        else:
            return array[start], array[end]

    return None


def getSumS(array, target):

    small = 0
    big = 1
    Sum = array[small] + array[big]

    while small < big:

        if Sum == target:
            print(array[small:big + 1])

            if big < len(array) - 1:
                big += 1
                Sum += array[big]
            continue

        if Sum < target and big < len(array) - 1:
            big += 1
            Sum += array[big]
        if Sum > target and small < big:
            Sum -= array[small]
            small += 1




def main():

    test_array = [1,2,4,7,11,15]
    target = 15

    start, end = getTarget(test_array, target)

    getSumS([1,2,3,4,5,6,7,8], target)

    print(start, end)



if __name__ == "__main__":
    main()