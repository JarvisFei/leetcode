
result = dict()

def countFre(Num, Sum):

    if Num == 0:
        result[Sum] =result.get(Sum, 0) + 1
        return

    for i in range(1,7):
        countFre(Num - 1, Sum + i)



def main():

    test_Num = 2

    countFre(test_Num, 0)


    print(result)


if __name__ == "__main__":
    main()