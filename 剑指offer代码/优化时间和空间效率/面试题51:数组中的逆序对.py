
def getCount(array):

    count = 0

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                count += 1
    return count






def main():
    test_array = [7,5,6,4]

    result = getCount(test_array)
    print(result)


if __name__ == "__main__":
    main()