class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


root = Node(10)

tempNode = root

import numpy as np
for i in np.random.randint(0,100,[10]):
    tempNode.next = Node(i)
    tempNode = tempNode.next
    print(i)
stack = []

print("")

while root:
    stack.append(root)
    root = root.next

while stack:
    res = stack.pop()
    print(res.val)
