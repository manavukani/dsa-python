from collections import deque


# TC: O(N×C)
# SC: O(C)
class Solution:
    def pageFaults(self, N, C, pages):
        count = 0
        q = deque()
        window = set()

        for page in pages:
            # Case 1: Page is not in cache
            if page not in window:
                count += 1
                # If cache is full, remove the least recently used page
                if len(q) == C:
                    removed = q.popleft()
                    window.remove(removed)
                # Add the new page
                q.append(page)
                window.add(page)
            else:
                # Case 2: Page is already in cache
                # Move the page to the most recently used position
                q.remove(page)
                q.append(page)

        return count


# ==================== OPTIMIZED SOLUTION - in real life ===========================
"""
- Fewer Operations: Direct removal of LRU page from the set avoids rearranging the entire deque.
- Scalability: Deque operations depend on shifting elements, set and dict approach becomes favorable for large dataset
- Memory Management: The set and dict implementation ensures better handling of the LRU logic without redundant operations, critical for performance-sensitive applications.
"""


class Solution:
    def pageFaults(self, N, C, pages):
        # Initialize memory (set), indexes (map), and page_faults counter
        memory = set()
        indexes = {}
        page_faults = 0

        for i in range(N):
            page = pages[i]
            # Case 1: Space is available in memory
            if len(memory) < C:
                if page not in memory:
                    memory.add(page)
                    page_faults += 1
                # Update the index of the page
                indexes[page] = i
            else:
                # Case 2: Memory is full
                if page not in memory:
                    # Find the least recently used (LRU) page
                    lru_page = min(memory, key=lambda p: indexes[p])
                    memory.remove(lru_page)  # Remove the LRU page
                    memory.add(page)  # Insert the current page
                    page_faults += 1
                # Update the index of the page
                indexes[page] = i

        return page_faults
