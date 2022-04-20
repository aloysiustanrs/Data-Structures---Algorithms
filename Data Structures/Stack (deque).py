from collections import deque

stack = deque()

stack.append(4)
stack.append(2)
stack.append(123)
stack.append(3)
stack.append(44)


stack.pop()

for i in stack:
    print(i)