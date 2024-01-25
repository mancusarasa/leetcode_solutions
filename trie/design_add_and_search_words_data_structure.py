#!/usr/bin/env python3
'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

'''


class Node:
    def __init__(self):
        self.children = [None for _ in range(ord('z') - ord('a') + 1)]
        self.defined = False
    
    def get_index(self, c):
        return ord(c) - ord('a')
    
    def get_or_create_child(self, c):
        index = self.get_index(c)
        if self.children[index] is None:
            self.children[index] = Node()
        return self.children[index]
    
    def get_child(self, c):
        index = self.get_index(c)
        return self.children[index]

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.get_or_create_child(c)
        node.defined = True


    def search(self, word: str) -> bool:
        return self._recursive_search(self.root, word)
    
    def _recursive_search(self, node, word):
        if node is None:
            return False
        if not word:
            return node.defined
        c = word[0]
        rest = word[1:]
        if c == '.':
            result = False
            for child in node.children:
                result = result or self._recursive_search(child, rest)
            return result
        else:
            return self._recursive_search(node.get_child(c), rest)
