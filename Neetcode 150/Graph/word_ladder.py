import collections


# STRIVER APPROACH IS BETTER
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
        # for all posn in word
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


# NEETCODE APPROACH
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        # adjancey map
        nei = collections.defaultdict(list)
        wordList.append(beginWord)  # not in list, so append

        # for each word => for each position we generate pattern
        for word in wordList:
            for j in range(len(word)):
                # exclude jth posn with *
                pattern = word[:j] + "*" + word[j + 1 :]

                # add word to that pattern -> pattern : list of word (all differ by 1 char)
                nei[pattern].append(word)

        # BFS
        visited = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
            # all words in queue
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                else:
                    for j in range(len(curr)):
                        pattern = curr[:j] + "*" + curr[j + 1 :]
                        # for all words for that pattern
                        for nextWord in nei[pattern]:
                            # check unvisited (helps exclude beginWord as well)
                            if nextWord not in visited:
                                visited.add(nextWord)
                                q.append(nextWord)

            # for each iterationn of BFS
            res += 1

        return 0
