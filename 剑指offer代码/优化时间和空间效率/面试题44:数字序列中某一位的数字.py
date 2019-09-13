

def getNum(N):


    if N <= 9:
        return N
    Sum = 9

    i = 1
    while Sum < N:
        if Sum + 9 * pow(10, i) * (i + 1) > N:

            result = pow(10, i) + (N - Sum - 1) // ( i + 1)

            return str(result)[(N - Sum - 1) % (i + 1)]

        else:
            Sum += 9 * pow(10, i) * (i + 1)

            i += 1



def main():
    test_N = 19

    result = getNum(test_N)

    print(result)



if __name__ == "__main__":
    main()