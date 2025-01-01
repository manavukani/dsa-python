class Stack:
    def __init__(self):
        self.top = -1
        self.arr = [0] * 500

    def push(self, x):
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return
        ans = self.arr[self.top]
        self.top -= 1
        return ans

    def top_ele(self):
        if self.top == -1:
            print("Stack is empty")
            return
        return self.arr[self.top]

    def size(self):
        return self.top + 1


# with a fixed size
class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 500
        self.arr = [0] * self.maxSize

    def push(self, x):
        if self.currSize == self.maxSize:
            print("Queue is full")
            return
        # if empty
        if self.end == -1:
            self.start = 0
            self.end = 0
        # somewere in the middle or at the end (modulus brings to start)
        else:
            self.end = (self.end + 1) % self.maxSize

        self.arr[self.end] = x
        self.currSize += 1

    def pop(self):
        if self.currSize == 0:
            print("Queue is empty")
            return
        # pop is from left - start
        ans = self.arr[self.start]
        # if only one element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return ans

    def top(self):
        if self.currSize == 0:
            print("Queue is empty")
            return
        return self.arr[self.start]

    def size(self):
        return self.currSize
