"""TRIE APPROACH"""


class TrieNode:
    def __init__(self):
        self.children = {}  # Stores the children nodes
        self.suggestions = []  # Stores up to 3 suggestions for the current prefix


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, product):
        node = self.root
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
            # Add the product to the suggestions if there are fewer than 3
            if len(node.suggestions) < 3:
                node.suggestions.append(product)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No matching prefix
            node = node.children[char]
        return node.suggestions


def suggestedProducts(products, searchWord):
    # Sort the products lexicographically
    products.sort()

    # Build the Trie
    trie = Trie()
    for product in products:
        trie.insert(product)

    result = []
    prefix = ""
    for char in searchWord:
        prefix += char
        # Search for suggestions in the Trie
        suggestions = trie.search(prefix)
        result.append(suggestions)

    return result


"""BINARY SEARCH APPROACH"""


def suggestedProducts(products, searchWord):
    # Sort the products lexicographically
    products.sort()

    result = []
    prefix = ""

    for char in searchWord:
        prefix += char
        # Find the first product that starts with the current prefix
        left = 0
        right = len(products) - 1
        while left <= right:
            mid = (left + right) // 2
            if products[mid].startswith(prefix):
                # Move left to find the first occurrence
                right = mid - 1
            elif products[mid] < prefix:
                left = mid + 1
            else:
                right = mid - 1

        # Now, left is the starting index of products that start with prefix
        suggestions = []
        for i in range(left, min(left + 3, len(products))):
            if products[i].startswith(prefix):
                suggestions.append(products[i])
            else:
                break

        result.append(suggestions)

    return result
