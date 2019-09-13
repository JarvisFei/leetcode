import sys
class Stack():
    def __init__(self):
        self.data = []
        self.min = []

    def pop(self):

        result = self.data[-1]
        self.data = self.data[:-1]

        if result == self.min[-1]:
            self.min = self.min[:-1]
        return result


    def push(self, val):

        self.data.append(val)

        if not self.min:
            self.min.append(val)
        else:
            if val <= self.min[-1]:
                self.min.append(val)
        return True


    def mindata(self):

        if len(self.min) == 0:
            return None
        return self.min[-1]

def main():
    test = [9,8,7,5,4,6,1,8]

    stack = Stack()

    for i in test:
        stack.push(i)
        print(i, stack.mindata())
    print()

    for i in range(8):

        print(stack.pop(),stack.mindata())



if __name__ == "__main__":
    main()