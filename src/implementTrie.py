#!/usr/bin/python

class TrieNode():
    def __init__(self,c=None):
        self.c = c
        self.children={}
        self.isLeaf = False
        
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        p = self.root
        for i in range(len(word)):
            if word[i] not in p.children:
                p.children[word[i]] = TrieNode(word[i])
            p = p.children[word[i]] 
        p.isLeaf = True
    def search(self, keyword):
        if keyword is None or len(keyword) == 0:
            return None
        p = self.root
        for i in range(len(keyword)):
            if keyword[i] in p.children:
                p = p.children[keyword[i]]
            else:
                return None
        if p.isLeaf is True:
            return keyword
        else:
            return None
    def startWith(self, prefix):
        if prefix is None or len(prefix) == 0:
            return None
        p = self.root
        for i in range(len(prefix)):
            if prefix[i] in p.children:
                p = p.children[prefix[i]]
            else:
                return False
        return True  
        
        
trie = Trie()
trie.insert('toy')
trie.insert('apple')
trie.insert('toilt')
children= trie.root.children
print trie.search("toy")
print trie.startWith('to')