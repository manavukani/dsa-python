# Floyd's Tortoise and Hare algorithm

# =========== BRUTE FORCE ============> store node in hash-map and keep count

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

'''
Time Complexity: O(N * 2 * log(N) )The algorithm traverses the linked list once, 
performing hashmap insertions and searches in the while loop for each node. 
The insertion and search operations in the unordered_map have a worst-case time complexity of O(log(N)). 
As the loop iterates through N nodes, the total time complexity is determined by the product of the traversal (O(N)) and
the average-case complexity of the hashmap operations (insert and search), resulting in O(N * 2 * log(N)). 

Space Complexity: O(N) The code uses a hashmap/dictionary to store encountered nodes, which can take up to O(N) additional space,
where 'n' is the number of nodes in the list. Hence, the spacecomplexity is O(N) due to the use of the map to track nodes.
'''

def brute(head):
    node_set = set()
    curr = head
    while curr is not None:
        if curr in node_set:
            return True
        node_set.add(curr)
        curr = curr.next
    return False

# =========== OPTIMAL - SLOW FAST POINTER ============> Time: O(N), Space: O(1)
def optimal(head):
    s = head
    f = head
    while f is not None and f.next is not None:
        s = s.next
        f = f.next.next
        if s == f:
            return True
    return False