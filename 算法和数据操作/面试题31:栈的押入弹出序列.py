
def judge(push, pop):

    if not push or not pop:
        return False

    stack = []

    while push:

        if push[0] == pop[0]:
            push = push[1:]
            pop = pop[1:]
        else:
            stack.append(push[0])
            push = push[1:]

    while stack:
        if stack.pop() == pop[0]:
            pop = pop[1:]
        else:
            return False
    return True



def main():

    test_push = [1,2,3,4,5]
    test_pop = [4,5,3,2,1]

    result = judge(test_push, test_pop)
    print(result)


if __name__ == "__main__":
    main()