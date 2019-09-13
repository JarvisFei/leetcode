
def F(string):

    if len(string) == 0:
        return 1

    if len(string) == 1:
        return 1


    if eval(string[:2]) >= 0 and eval(string[:2]) <= 25:
        return F(string[1:]) + F(string[2:])
    else:
        return F(string[1:])


def F1(string):

    if len(string) == 0:
        return 0
    if len(string) == 1:
        return 1

    f1 = 1
    f2 = 1
    f3 = 0

    for i in range(1, len(string), 1):
        if eval(string[i - 1] + string[i]) >= 0 and eval(string[i - 1] + string[i]) <= 25:
            f3 = f2 + f1
        else:
            f3 = f2
        f2, f1 = f3, f2
    return f3


def main():
    test = "12258"

    result = F(test)

    print(result)


    print(F1(test))


if __name__ == "__main__":
    main()
