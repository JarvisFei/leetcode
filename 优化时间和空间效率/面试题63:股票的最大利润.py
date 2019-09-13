
def getMaxEarning(array):

    if not array:
        return

    result = [0] * len(array)

    minP = array[0]

    for i in range(0,len(array)):

        if array[i] <= minP:
            minP = array[i]
            result[i] = 0
            continue
        result[i] = array[i] - minP

    print(result)
    return max(result)






def main():

    test_array = [9,11,8,5,7,12,16,14]

    result = getMaxEarning(test_array)

    print(result)



if __name__ == "__main__":
    main()