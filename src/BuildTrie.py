#!/usr/bin/python

'''
Implement a trie with insert, search, and startsWith methods.
'''

class TrieNode():
    def __init__(self,value=None):
        self.value=value
        self.children = dict()
        self.isLeaf=False
        
class Trie():
    def __init__(self):
        self.root=TrieNode()
    def insert(self, wordList):
        p = self.root
        for word in wordList:
            for i in range(len(word)):
                if p.children.get(word[i]) is None:
                    p.children[word[i]]=TrieNode(word[i])
                p=p.children[word[i]]
                if i == len(word)-1:
                    p.isLeaf=True
    def search(self, keyword):
        if keyword is None or len(keyword) == 0:
            return None
        p = self.root
        for i in range(len(keyword)):
            if p.children.get(keyword[i]) is None:
                return None
            else:
                p=p.children[keyword[i]]
        if p.isLeaf == True:
            return keyword
        return None
'''
class Trie:
    def buildTrie(self, wordList):
        trie = {}
        for word in wordList:
            node = trie
            for letter in word:
                child = node.get(letter)
                if child is None:
                    child = {}
                    node[letter] = child
                node = child
        return trie
'''
if __name__ == '__main__':
    wordList =['buy','but','sell','see']
    trie = Trie()
    trie.insert('toy')
    trie.insert('apple')
    trie.insert('toilt')
    print trie.root.children
    print trie.search('toy')
    #print trie.buildTrie(wordList)