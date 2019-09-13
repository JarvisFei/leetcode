
def getMaxValue(matrix):

    if not matrix:
        return 0

    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):
            if i - 1 >= 0 and j - 1 >=0:
                matrix[i][j] = max([matrix[i - 1][j], matrix[i][j - 1]]) + matrix[i][j]
            elif i - 1 >= 0 and j - 1 < 0:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j]
            elif i - 1 < 0 and j - 1 >= 0:
                matrix[i][j] = matrix[i][j - 1] + matrix[i][j]
            else:
                matrix[i][j] = matrix[i][j]

    return matrix[row - 1][col - 1]


def main():

    test_matrix = [[1,10,3,8],
                   [12,2,9,6],
                   [5,7,4,11],
                   [3,7,16,5]]


    maxVale = getMaxValue(test_matrix)

    print(maxVale)



if __name__ == "__main__":
    main()