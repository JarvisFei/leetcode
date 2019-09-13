import time
#解法1，这个是时间复杂度是o(N),但是空间复杂度也是o(N),因为使用了一个哈希表作为额外使用空间
def GetRepNum(N):
    res = set()

    for i in N:
        if i not in res:
            res.add(i)
        else:
            return i

    return None

start = time.perf_counter()
print(GetRepNum([2,3,1,0,2,5,3]))
print(time.perf_counter() - start)


#解法2，考虑第i个数的值，是否与这个值作为下标的那个值相等，如果相等即有重复。主要考察的是数组下标的运用

def GetreNum(N):

    #第一步，处理无效输入样例
    if len(N) == 0:
        return False
    for i in N:
        if i < 0 or i >= N:
            return False

    #第二步，开始处理输入和核心逻辑
    for i in range(len(N)):
        while i != N[i]:
            if N[i] == N[N[i]]:
                return N[i]
            else:
                N[i], N[N[i]] = N[N[i]], N[i]
    return False

start = time.perf_counter()
print(GetRepNum([2,3,1,0,2,5,3]))
print(time.perf_counter() - start)