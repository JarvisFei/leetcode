
def getMax(array, K):

    if len(array) == 1:
        return array

    if len(array) < K:
        K = len(array) - K


    while K:
        array = array[1:] + array[0:1]
        K -= 1

    return array


def getMax(array, K):

    if K >= len(array):
        return max(array)

    result = []

    for i in range(K - 1,len(array)):

        result.append(max(array[i - 2 : i + 1]))

    return result




def main():
    test_array = [2,3,4,2,6,2,5,1]
    K = 3

    result = getMax(test_array, K)

    print(result)



if __name__ == "__main__":
    main()