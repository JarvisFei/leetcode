
#所有题目，第一步写测试样例，考虑功能测试和边界测试，还有异常测试
test = [3,4,5,1,2]
test1 = [1,2,3,4,5]
test2 = [1]
target = 1

#二分法查找
def search(array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) / 2
        mid = int(mid)

        if array[mid] == target:
            return True

        if array[mid] > target:
            end = mid
        if array[mid] < target:
            start = mid

    return False

print(search(test1))

#旋转数组最小值

def search(array):
    #如果不符合要求的数组，不处理
    if array[-1] > array[0]:
        return array[0]

    #开始处理符合要求的数组
    start = 0
    end = len(array) - 1

    while start <= end:

        if start == end:
            return array[start]
        if start == end - 1:
            return array[end]

        mid = (start + end) // 2

        if array[mid] > array[start]:
            start = mid
        elif array[mid] < array[start]:
            end = mid
        elif array[start] == array[end]:
            return lineSearch(array,start,end)

def lineSearch(array, start, end):
    max = 0
    for i in range(start, end + 1):
        if array[i] > max:
            max = array[i]
    return max()



print(search(test2))

