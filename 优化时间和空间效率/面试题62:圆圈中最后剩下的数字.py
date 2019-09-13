
def deleteNum(array, K):

    while len(array) > 1:
        K = K % len(array)

        del array[K-1]
        array = array[K-1:] + array[:K-1]


        print(array)


    return array



def main():

    test_array = [0,1,2,3,4]
    K = 3

    result = deleteNum(test_array, K)

    print(result)


if __name__ == "__main__":
    main()