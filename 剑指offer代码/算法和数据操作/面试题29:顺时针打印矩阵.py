
def printMatrix(array, startI, startJ, visited):

    row = len(array)
    col = len(array[0])

    index = startI * col + startJ


    if index not in visited and startI < row and startI >= 0 and startJ < col and startJ >= 0:
        print(array[startI][startJ])
        visited.add(index)

        # if len(visited) == row * col:
        #     return

        printMatrix(array, startI, startJ + 1, visited)
        printMatrix(array, startI + 1, startJ, visited)
        printMatrix(array, startI, startJ - 1, visited)
        printMatrix(array, startI - 1, startJ, visited)




def main():
    testMatrix = [[1,2,3,4,5,6],
                  [7,8,9,10,11,12],
                  [13,14,15,16,17,18]]
    visited = set()
    printMatrix(testMatrix, 0, 0,visited)


if __name__ == "__main__":
    main()