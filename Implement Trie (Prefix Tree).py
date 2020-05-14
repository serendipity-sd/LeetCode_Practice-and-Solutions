class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isword = False
        self.children = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
            
        node.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
            
        return node.isword 
            

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
