from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isTerminal = False
        self.fail = None
        self.output = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isTerminal = True
        curr.output.append(word)

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.isTerminal

    def build_fail_links(self):
        queue = deque()
        self.root.fail = None  # Корень не имеет fail-ссылки

    