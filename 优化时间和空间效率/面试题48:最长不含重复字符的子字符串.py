
import sys
def getMaxSubStr(string):

    visited = {}
    result = [0] * len(string)

    visited[string[0]] = 0
    result[0] = 0

    for i in range(1,len(string)):

        if string[i] in visited.keys():
            if visited[string[i]] >= result[i - 1]:
                result[i] = visited[string[i]] + 1
                visited[string[i]] = i
            else:
                result[i] = result[i - 1]
                visited[string[i]] = i
        else:
            result[i] = result[i - 1]
            visited[string[i]] = i

    result = [index - result[index] + 1 for index in range(len(result))]

    return result




def main():
    test = "arabcacfr"
    result = getMaxSubStr(test)

    print(result)


if __name__ == "__main__":
    main()