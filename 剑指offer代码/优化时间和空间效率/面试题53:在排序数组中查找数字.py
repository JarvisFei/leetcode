
def getNum(array, target):

    start = 0
    end = len(array) - 1

    mid = (end + start)//2

    while start <= end:

        if array[mid] == target and array[mid - 1] < target:
            first = mid
            break

        if array[mid] >= target:
            end = mid
        if array[mid] < target:
            start = mid
        mid = (end + start)//2

    start = 0
    end = len(array) - 1

    mid = (end + start) // 2

    while start <= end:

        if array[mid] == target and array[mid + 1] > target:
            second = mid
            break

        if array[mid] > target:
            end = mid
        if array[mid] <= target:
            start = mid
        mid = (end + start) // 2
    return second - first + 1







def main():
    test_array = [1,2,3,3,3,3,3,4,5]
    result = getNum(test_array, target = 3)
    print(result)


if __name__ == "__main__":
    main()