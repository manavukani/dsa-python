from queue import LifoQueue


# TC: O(N)
# SC: O(2N) = O(N)
class QueueWith2Stacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        # pop and push all element of s1 -> s2
        # push new ele to s1
        # pop and push all elements back to s1
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def top(self):
        return self.s1[-1]

    def size(self):
        return len(self.s1)

    def empty(self):
        return not self.s1

q = QueueWith2Stacks()
q.push(4)
q.push(3)
q.push(2)
q.push(5)
print(q.top())
print(q.pop())
print(q.top())


# TC: O(1) Amortized (since we are not always moving elements)
# SC: O(2N) = O(N)
class QueueOptimal:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        if self.output:
            # return pop
            return self.output.pop()
        else:
            # ip -> op
            while self.input:
                self.output.append(self.input.pop())
            # return pop
            return self.output.pop()

    def top(self):
        if self.output:
            # return top
            return self.output[-1]
        else:
            # ip -> op
            while self.input:
                self.output.append(self.input.pop())
            # return top
            return self.output[-1]
    
    def size(self):
        return len(self.input) + len(self.output)
    
    def empty(self):
        return not self.input and not self.output

