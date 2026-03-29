class Node:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.term = False
class PrefixTree:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        self.insertUtil(self.root, word)

    def insertUtil(self, node, word):
        if not word:
            node.term = True
            return
        char = ord(word[0]) - ord('a')
        if not node.children[char]:
            node.children[char] = Node(word[0])        
        # if len(word) == 1:
        #     node.children[char].term = True
        self.insertUtil(node.children[char], word[1:])



    def search(self, word: str) -> bool:
        return self.searchUtil(self.root, word)

    def searchUtil(self, node, word) -> bool:
        if not word:
            return False
            
        char = ord(word[0]) - ord('a')
        if not node.children[char]:
            return False
        if len(word) == 1:
            return node.children[char].term
        return self.searchUtil(node.children[char], word[1:])


    def startsWith(self, prefix: str) -> bool:
        return self.startsWithUtil(self.root, prefix)
    def startsWithUtil(self, node, word) -> bool:
        if not word:
            return True

        char = ord(word[0]) - ord('a')
        if not node.children[char]:
            return False
        return self.startsWithUtil(node.children[char], word[1:])