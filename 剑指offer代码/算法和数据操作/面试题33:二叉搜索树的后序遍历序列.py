

def judgePostOrder(array):


    if len(array) < 3:
        return True


    root = array[-1]
    start = -1
    end = len(array) - 1

    while start <= end:

        while start + 1 < end and array[start + 1] < root:
            start += 1
        while start < end - 1 and array[end - 1] > root:
            end -= 1

        if start + 1 == end:
            if judgePostOrder(array[0:start+1]) and judgePostOrder(array[end:-1]):
                return True
        else:
            return False


    return False



def main():
    test = [5,7,6,9,11,10,8]
    test = [7,4,6,5]

    result = judgePostOrder(test)

    print(result)



if __name__ == "__main__":
    main()