import functools

def cmp(a, b):

    a = str(a)
    b = str(b)

    while True:

        if not a and not b:
            return 0

        if not a:
            return 1

        if not b:
            return -1

        if a[0] == b[0]:
            a = a[1:]
            b = b[1:]
            continue
        if a[0] > b[0]:
            return 1
        if a[0] < b[0]:
            return -1

    return 0

def getMin(array):

    result = sorted(array, key=functools.cmp_to_key(cmp))

    print(eval("".join([str(i) for i in result])))


def main():

    test_array = [3,32,321]
    getMin(test_array)



if __name__ == "__main__":
    main()
