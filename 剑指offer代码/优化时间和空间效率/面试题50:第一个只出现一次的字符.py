
def getFNum(array):

    visited_record = set()
    visited_once = set()

    result = None

    for i in array:

        if i in visited_record:
            if i in visited_once:
                visited_once.remove(i)
        else:
            visited_record.add(i)
            visited_once.add(i)

    for i in array:

        if i in visited_once:
            return i



def main():
    test_array = "abaccdeff"

    result = getFNum(test_array)

    print(result)



if __name__ == "__main__":
    main()