class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count+=1
    def get_prefix_score(self, word):
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.count
        return score
         
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        answer = []
        for word in words:
            answer.append(trie.get_prefix_score(word))
        return answer
        
