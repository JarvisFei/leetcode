
#题目是从一个二维数组中查找一个数。算法的时间复杂度是O（m + n）
def Exist(N, target):
    if len(N) == 0:
        return False

    row = len(N)
    col = len(N[0])
    i = 0
    j = col - 1
    while i < row and j >= 0:
        print(i,j)
        if N[i][j] > target:
            j -= 1
        elif N[i][j] < target:
            i += 1
        else:
            return True

    return False


N = [[1,2,8,9],
     [2,4,9,12],
     [4,7,10,13],
     [6,8,11,15]]

print(Exist([],-1))

