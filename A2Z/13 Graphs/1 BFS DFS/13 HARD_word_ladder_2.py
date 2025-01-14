# one of those questions which you need to see otherwise can't do

# TODO: print all the possible paths with shortest length

from collections import deque

"""
TC: depends on case to case 
But gives TLE on Leetcode, but logic works fine for interview
"""

"""
Approach:
1. Use BFS to explore all possible paths.
2. Maintain queue to store the current paths being explored and add further calls.
3. Use a set to keep track of words used at the current level
        - Ensure that words used in the current level are removed from the wordList in the next level to avoid cycles.
        - REASON: multiple path may use same word for same level, so remove afterwards
4. For last word in the current path, generate all possible transformations
5. If a transformation is valid (exists in wordList), add it to the current path and continue exploring.
6. If a path reaches endWord, add it to the result list.
"""


def solve(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    q = deque()
    q.append([beginWord])

    usedOnLevel = set()

    level = 0

    ans = []

    while q:
        currentPath = q.popleft()

        # Remove used words after processing all paths of the current level
        if len(currentPath) > level:
            level += 1
            for w in usedOnLevel:
                wordSet.discard(w)  # IMP: use discard instead of remove to avoid errors
            usedOnLevel.clear()  # clear used words for the next level

        word = currentPath[-1]

        # store the path if it reaches the endWord
        if word == endWord:
            #  first valid path
            if len(ans) == 0:
                ans.append(currentPath)
            # not first, but size same as previous one
            elif len(ans[0]) == len(currentPath):
                ans.append(currentPath)

        # generate all possible transformations
        for i in range(len(word)):
            original = word[i]
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + ch + word[i + 1 :]
                if newWord in wordSet:
                    # IMPP!!! ===> create a new path to avoid mutating the current one
                    # got a valid word in path, add to queue
                    newPath = currentPath + [newWord]
                    q.append(newPath)
                    usedOnLevel.add(newWord)

    return ans


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solve(beginWord, endWord, wordList))
