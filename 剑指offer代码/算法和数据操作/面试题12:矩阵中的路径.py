"""
#图的深度优先和广度优先算法
"""

#首先，使用矩阵存储图的时候

a = set()
flag = False

def DFS(matrix, i, j, visted, path):
    global flag
    if not matrix:
        return

    if not path:
        flag = True
        return


    if matrix[i][j] == path[0]:
        path = path[1:]
        visted.add(i * len(matrix) + j)
    else:
        return

    i += 1
    if i  >=0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix[0]) - 1 and i * len(matrix) + j not in visted:
        visted.add(i * len(matrix) + j)
        DFS(matrix, i, j, visted, path)
        visted.remove(i * len(matrix) + j)
    i -= 1

    i -= 1
    if i >=0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix[0]) - 1 and i * len(matrix) + j not in visted:
        visted.add(i * len(matrix) + j)
        DFS(matrix, i, j, visted, path)
        visted.remove(i * len(matrix) + j)
    i += 1

    j -= 1
    if i >=0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix[0]) -1 and i * len(matrix) + j not in visted:
        visted.add(i * len(matrix) + j)
        DFS(matrix, i, j, visted, path)
        visted.remove(i * len(matrix) + j)
    j += 1

    j += 1
    if i >=0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix[0]) - 1 and i * len(matrix) + j not in visted:
        visted.add(i * len(matrix) + j)
        DFS(matrix, i, j, visted, path)
        visted.remove(i * len(matrix) + j)
    j -= 1

test_matrix = [["a", "b", "t", "g"],
               ["c", "f", "c", "s"],
               ["j", "d", "e", "h"]]
DFS(test_matrix, 0, 1, set(), "bfch")
print(flag)


