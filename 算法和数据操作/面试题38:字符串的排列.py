

"""
一个伟大的思路
"""
def permulation(result, array):

    if not array:
        print(result)
        return

    baseArray = array

    visited = set()
    for i in array:
        if i not in visited:
            visited.add(i)
            array = baseArray.replace(i, "",1)
            permulation(result + i, array)


def combination(result, array, m):
    if m == 0:
        print(result)
        return

    if len(array) == 0:
        return

    basearray = array
    char = array[0]
    array = array[1:]

    combination(result + char, array, m - 1)
    array = basearray[1:]
    combination(result, array, m)



def main():

    # permulation("","abca")
    combination("", "abc",2)

if __name__ == "__main__":

    test = set()


    main()


