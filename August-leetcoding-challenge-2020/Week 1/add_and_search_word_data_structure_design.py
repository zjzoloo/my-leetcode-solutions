# Author: Zoljargal Gantumur
# Runtime: 496 ms
# Memory Usage: 25.8 MB 

# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string 
# containing only letters a-z or .. A . means it can represent any one letter.

# Example:
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        reduce(lambda node,c: node.setdefault(c,{}), word, self.d)['$'] = None


    def search(self, word: str, n: dict = None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return(any(self.search(word[1:],v)for v in((n or self.d).values()if word[0]=='.'else[(n or self.d).setdefault(word[0],{})])if v)if word else'$'in (n or self.d))
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
