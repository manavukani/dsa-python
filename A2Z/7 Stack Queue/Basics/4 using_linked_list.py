class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        # link new node to the current top
        new_node.next = self.top
        # top is now new node
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        # popped value -> current top
        top_value = self.top.value
        # update top node to top's next
        self.top = self.top.next
        self.size -= 1
        return top_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value

    def get_size(self):
        return self.size


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        # empty -> new node is front
        if self.is_empty():
            self.front = new_node
        # not empty -> link rear to new node
        else:
            self.rear.next = new_node
        # update rear to new node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        front_value = self.front.value
        self.front = self.front.next
        self.size -= 1
        return front_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.value

    def get_size(self):
        return self.size


# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print("Top element:", stack.peek())
# print("Stack size:", stack.get_size())
# print("Popped:", stack.pop())
# print("Stack size after pop:", stack.get_size())

# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print("Front element:", queue.peek())
# print("Queue size:", queue.get_size())
# print("Dequeued:", queue.dequeue())
# print("Queue size after dequeue:", queue.get_size())
