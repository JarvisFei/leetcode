
def maxSum(array, sum):

    if len(array) == 0:
        return sum

    result = [0] * len(array)
    for i in range(len(array)):
        if i == 0:
            result[0] = array[0]
            continue

        if result[i - 1] > 0:
            result[i] = result[i - 1] + array[i]
        else:
            result[i] = array[i]
    return max(result)




def main():
    test_array = [1,-2,3,10,-4,7,2,-5]

    result = maxSum(test_array, 0)

    print(result)


if __name__ == "__main__":
    main()