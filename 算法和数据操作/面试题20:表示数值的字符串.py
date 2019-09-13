
def Judge(string):
    try:
        int(eval(string))
    except:
        return False

    return True


def main():

    test_function = "3.14"
    test_boundary = ""
    print(Judge(test_function))



if __name__ == "__main__":
    main()