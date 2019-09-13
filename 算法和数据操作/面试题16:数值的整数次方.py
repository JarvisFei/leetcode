
#统计一个整数二进制中1的个数

def CountOne(Num):
    try:
        assert type(Num) == int
    except:
        return "Error"
    if Num >= 0:
        count = 0
    else:
        count = 1
        Num = -Num


    while Num:

        count += 1
        Num = (Num - 1) & Num

    return count

def main():
    test_function = 7
    test_bouddary1 = 0
    test_bouddary2 = -7


    result = CountOne(test_bouddary2)
    print(result)

#数值的整数次方：
def main():
    test_function = 4, 5
    test_function = 4, -5
    test_boundary = 0, 0
    test_boundary = 0, -1

    print(Power(4, 2))


def Power(base, exponent):

    if exponent == 0:
        return 1

    if base == 0:
        return None


    exp = abs(exponent)

    if exp == 1:
        return base

    temp = exp

    result = base
    exp = exp >> 1
    while exp:
        result = result * result
        exp = exp >> 1
        print(result, exp)

    if temp % 2 == 1:
        result *= base


    if exponent > 0:
        return result
    else:
        return 1.0/result



if __name__ == "__main__":
    main()
