# capacity given
# get, put in O(1)
# if capacity full, remove LFU item
# if multiple with least freq => remove LRU item

class LFUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.freq = 1
            self.prev = None
            self.next = None

    class DoublyLinkedList:
        def __init__(self):
            self.head = LFUCache.Node(0, 0)  # Dummy head
            self.tail = LFUCache.Node(0, 0)  # Dummy tail
            self.head.next = self.tail
            self.tail.prev = self.head

        def append(self, node):
            """Add node to the front (right after head)."""
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

        def remove(self, node):
            """Remove the given node."""
            node.prev.next = node.next
            node.next.prev = node.prev

        def pop(self):
            """Remove the last node (just before the tail)."""
            if self.head.next == self.tail:  # List is empty
                return None
            last_node = self.tail.prev
            self.remove(last_node)
            return last_node

        def is_empty(self):
            return self.head.next == self.tail

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.nodeMap = {}  # key -> node
        self.freqMap = {}  # freq -> DoublyLinkedList

    def _update(self, node):
        """Update the frequency of a node."""
        freq = node.freq
        self.freqMap[freq].remove(node)
        if self.freqMap[freq].is_empty() and freq == self.minFreq:
            self.minFreq += 1

        node.freq += 1
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = self.DoublyLinkedList()
        self.freqMap[node.freq].append(node)

    def get(self, key):
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self._update(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                # Evict least frequently used node
                to_remove = self.freqMap[self.minFreq].pop()
                del self.nodeMap[to_remove.key]
                self.size -= 1

            # Insert new node
            new_node = self.Node(key, value)
            self.nodeMap[key] = new_node
            if 1 not in self.freqMap:
                self.freqMap[1] = self.DoublyLinkedList()
            self.freqMap[1].append(new_node)

            self.minFreq = 1
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)