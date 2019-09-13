
def getUglyNum(Num):

    count = 1

    index = 1

    while count <= Num:

        if count == Num:
            print(index)

        index += 1

        temp = index

        while temp % 2:
            temp = temp / 2
        while temp % 3:
            temp = temp / 3
        while temp % 5:
            temp = temp / 5
        if temp == 0:
            count += 1





def main():
    test_num = 1500

    result = getUglyNum(test_num)

    print(result)


if __name__ == "__main__":
    main()