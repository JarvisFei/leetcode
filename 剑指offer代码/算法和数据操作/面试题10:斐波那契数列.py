#递归写法

def F(first, second, N):
    if N < 3:
        return 1

    if N == 3:
        return first + second

    return F(second, first + second, N - 1)

print(F(1,1,10))

#非递归写法

N = 10
first = 1
second = 1
result = 0
for i in range(3,N + 1,1):
    result = first + second
    first, second = second, result
print(result)

#最快的一种解法，递归使用公式。



#延伸题目1，一直青蛙，每次可以调两级台阶也可以跳一级台阶，请问，n级台阶有多少中跳法？F(n) = F(n-1) + F(n-2)

#延伸题目2，一直青蛙，每次可以跳1、2、3。。。n级，请问，n级台阶有多少中跳法？F(n) = F(n-1) + F(n - 2) + ... + F(0)


#延伸题目3，用一个小的矩形1X2，无重叠覆盖一个2X9的大矩形，也是斐波那契数列

f_list = [lambda x:x**i for i in range(5)]
print("")
print(f_list[1](3))

print([f_list[j](10) for j in range(5)])
print(10**2)

