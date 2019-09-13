
def judge(array):

    if len(array) != 5:
        return None


    #排序
    array = sorted(array)

    zero_num = array.count(0)

    if zero_num == 0:
        for i in range(1, len(array)):
            if array[i] - array[i - 1] == 1:
                continue
            else:
                return False
        return True
    else:

        count_gap = 0
        for i in range(1, len(array)):
            if array[i] == 0:
                continue
            else:
                if array[i - 1] != 0:
                    count_gap += array[i] - array[i - 1] - 1
        if count_gap <= zero_num:
            return True
        else:
            return False

    return 0


def main():

    test_array = [0,2,9,3,5]

    result = judge(test_array)

    print(result)




if __name__ == "__main__":
    main()
