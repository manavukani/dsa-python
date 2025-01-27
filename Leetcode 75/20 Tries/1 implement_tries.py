class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        inserts the string word into the trie.
        """
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        """
        returns
        - True if the string word is in the trie,
        - False otherwise.
        """
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        # check the last char is end or not
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        returns:
        - True if if there is a previously inserted string word that has the prefix prefix,
        - False otherwise.
        """
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        # doesn't matter if its end or not
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
