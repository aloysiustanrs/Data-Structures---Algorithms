class ArrayStack:

    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if not self.len() == 0:
            return self.data[-1]

    def len(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0


if __name__ == "__main__":

    stack = ArrayStack()

    stack.push(77)
    stack.push(3)
    stack.push(5)
    stack.push(1)
    stack.push(222)

    print(stack.peek())
