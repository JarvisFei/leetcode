def Power(baseNum, exponent):
    if exponent == 0:
        return 1
    if baseNum == 0 and exponent > 0:
        return 0
    if baseNum == 0 and exponent < 0:
        return "Error"


    base = baseNum
    exp = abs(exponent)
    #
    if exp == 1:
        return baseNum

    exp = exp >> 2

    while exp > 0:
        base = base * base
        exp = exp >> 2


    if exponent % 2 == 1:
        base *= baseNum

    if exponent < 0:
        return 1.0 / base

    return base


def main():
    test_function = 2,5

    test_boundary = 2,-5
    test_boundary = 0, -5
    test_boundary = 2, 0
    test_boundary = 0, 0

    result = Power(0,1)
    print(result)


if __name__ == "__main__":

    print(3&1)
    main()

