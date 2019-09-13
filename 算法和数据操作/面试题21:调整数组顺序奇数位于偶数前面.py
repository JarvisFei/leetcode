
def Sort(array):

    if len(array) <= 1:
        return array

    start = 0
    end = len(array) - 1

    while start < end:

        while array[start] & 1:
            start += 1
        while not array[end] & 1:
            end -= 1
        array[start], array[end] = array[end], array[start]




def main():

    test_function = [1,2,3,4,5,6,7,8,9,10]

    Sort(test_function)
    print(test_function)


if __name__ == "__main__":
    main()