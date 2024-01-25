#!/usr/bin/env python3
'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''

class Trie:
    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            current_node = current_node.extend(char)
        current_node.defined = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for c in word:
            current_node = current_node.get_child(c)
            if current_node is None:
                return False
        return current_node.defined

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for c in prefix:
            current_node = current_node.get_child(c)    
            if current_node is None:
                return False
        return self._has_key(current_node)
    
    def _has_key(self, node):
        if node is None:
            return False
        if node.defined:
            return True
        for child in node.children:
            if self._has_key(child):
                return True
        return False
        
    class Node:
        def __init__(self):
            self.defined = False
            self.children = [None for i in range(ord('z')+1-ord('a'))]

        def get_index(self, c):
            return ord(c) - ord('a')

        def extend(self, c):
            index = self.get_index(c)
            if self.children[index] is None:
                self.children[index] = Trie.Node()
            return self.children[index]

        def get_child(self, c):
            index = self.get_index(c)
            return self.children[index]
