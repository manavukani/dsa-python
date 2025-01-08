# one of those questions which you need to see otherwise can't do

# print all the possible paths with shortest length

from collections import deque

"""
TC: depends on case to case 
But gives TLE on Leetcode, but logic works fine for interview
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
        # REASON: multiple path may use same word for same level, so we remove in next level
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
