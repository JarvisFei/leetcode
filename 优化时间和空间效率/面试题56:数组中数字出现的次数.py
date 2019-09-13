
def getTwoNum(array):

    visited = set()

    for i in array:
        if i not in visited:
            visited.add(i)
        else:
            visited.remove(i)

    return visited



def main():
    test_array = [2,4,3,6,3,2,5,5]

    result = getTwoNum(test_array)

    print(result)
    
    print(bin(12))



if __name__ == "__main__":
    main()