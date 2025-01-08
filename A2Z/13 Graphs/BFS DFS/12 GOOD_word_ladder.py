import collections

# give number of steps to reach from beginWord to endWord using only those in wordList

"""
Approach:
    1. Use a queue (BFS) to store words and steps count.
    2. Pop each pair from queue and generate all possible one-character transformations for word.
    3. If a valid transformed word appears in the set, remove it (to avoid revisiting) and push it into the queue, with inc step count.
    4. Continue until the endWord is reached or no more transformations are possible.
"""

def ladderLength(beginWord, endWord, wordList):
    q = collections.deque()
    q.append((beginWord, 1))
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    """TC = O(number of words in wordList) = O(N)"""
    while q:
        word, steps = q.popleft()

        # if word reached
        if word == endWord:
            return steps

        """TC = O(wordLength * 26)"""
        # generate all possible transformations
        for i in range(len(word)):
            original = word[i]

            # try all ch and see if newWord exist in wordSet
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + ch + word[i + 1 :]

                # if exists --> remove from set and do BFS for it
                if newWord in wordSet:
                    wordSet.remove(newWord)
                    q.append(
                        (newWord, steps + 1)
                    )  # increase count since we used that word
    return 0


wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength("hit", "cog", wordList))  # 5

# TC = O(N * word Length * 26)  -- assuming set lookup is O(1) and not logN
# SC = O(N) -- set and queue
