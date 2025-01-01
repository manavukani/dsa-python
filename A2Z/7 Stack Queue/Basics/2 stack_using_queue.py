from queue import Queue

# using 2 queues
class StackWith2Queues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        """
        1. Push the element to the queue 1.
        2. Dequeue all elements from queue 1 and enqueue them into queue 2.
        This ensures the newly added element is at the front.
        3. Swap the queues so that queue 2 becomes queue 1.
        """
        self.q1.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.get()

    def top(self):
        return self.q1.queue[0]

    def size(self):
        return self.q1.qsize()

class StackWith1Queue:
    def __init__(self):
        self.q = Queue()
        
    '''
    1. Push the element to the queue
    2. Pop the first n-1 ele (front) and push it to back
        - now 'new' element will be at the front (top)
    '''
    def push(self, x):
        self.q.put(x)
        # pop the first n-1 elements 
        for _ in range(self.q.qsize() - 1):
            self.q.put(self.q.get())

    def pop(self):
        n = self.q.get()
        return n

    def top(self):
        return self.q.queue[0]

    def size(self):
        return self.q.qsize()

    def empty(self):
        return self.q.empty()


# Test
s = StackWith1Queue()
s.push(1)
s.push(2)
print(s.top())
print(s.pop())
print(s.empty())
