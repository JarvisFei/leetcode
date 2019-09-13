
class Queue:
    def __init__(self):
        """
        初始化队列
        """
        self.stack1 = []
        self.stack2 = []
        self.dataFlag = "1"



    def pop(self):
        self.move("2")
        if not self.stack2:
            return None
        return self.stack2.pop()


    def push(self,data):
        self.move("1")
        self.stack1.append(data)

    def move(self,flag):
        if flag == self.dataFlag:
            return
        if self.dataFlag == "1":
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
            self.dataFlag = "2"
        elif self.dataFlag == "2":
            self.stack1 = self.stack2[::-1]
            self.stack2 = []
            self.dataFlag = "1"
    def isEmpty(self):
        if not self.stack1 and not self.stack2:
            return True
        return False

queue = Queue()
test = [1,2,3,4,5,6]

for i in test:
    queue.push(i)

while not queue.isEmpty():
    print(queue.pop())
