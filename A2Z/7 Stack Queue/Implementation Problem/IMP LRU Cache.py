# capacity given
# get, put in O(1)
# if capacity full, remove least recently used item

# https://youtu.be/xDEuM5qa0zg

'''

Size = 3

HEAD <-----------------> TAIL

insert(2,6)

HEAD <----> 2,6 <----> TAIL

insert(1,5)

HEAD <----> 1,5 <----> 2,6 <----> TAIL

insert(4,7)

HEAD <----> 4,7 <----> 1,5 <----> 2,6 <----> TAIL

get(2) => remove and insert at front

HEAD <----> 2,6 <----> 4,7 <----> 1,5 <----> TAIL

insert(5,8) => remove last element and insert at front (WHEN CAPACITY = FULL)

HEAD <----> 5,8 <----> 2,6 <----> 4,7 <----> TAIL

'''


class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}  # key -> node
        self.head = self.Node(0, 0)  # dummy head node
        self.tail = self.Node(0, 0)  # dummy tail node
        self.head.next = self.tail  # initially connect head to tail
        self.tail.prev = self.head  # initially connect tail to head

    def get(self, key):
        # check exist
        if key in self.map:
            node = self.map[key]
            # accessed -> move to front
            self._remove(node)
            self._insert(node)
            return node.value
        # not exist
        return -1

    def put(self, key, value):
        # remove if already exist
        if key in self.map:
            self._remove(self.map[key])
        # capacity full -> remove last node (tail.prev)
        if len(self.map) == self.capacity:
            self._remove(self.tail.prev)
        # insert new node (at front - IMPORTANT)
        self._insert(self.Node(key, value))

    # utility functions
    def _remove(self, node):
        # save memory
        del self.map[node.key]
        # prevNode = node.prev
        # nextNode = node.next
        # prevNode.next = nextNode
        # nextNode.prev = prevNode

        # same but concise
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        # create new entry in map
        self.map[node.key] = node
        # assign next for new node -> head's next
        node.next = self.head.next
        # assign next's prev -> new node
        node.next.prev = node
        # assign head's next -> new node
        self.head.next = node
        # assign new node's prev -> head
        node.prev = self.head

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
