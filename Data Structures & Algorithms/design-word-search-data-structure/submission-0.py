
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(i, curr):
            if i == len(word):
                if curr.word:
                    return True
                else:
                    return False
            
            if word[i] != ".":
                if word[i] not in curr.children:
                    return False
                else:
                    if dfs(i + 1, curr.children[word[i]]):
                        return True
                    return False
                    
            else:
                for j in curr.children:
                    if dfs(i + 1, curr.children[j]):
                        return True
                return False

        return dfs(0, curr)
        
