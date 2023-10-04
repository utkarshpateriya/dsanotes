class Node:
    def __init__(self, val):
        self.val = val
        for i in range(26):
            self.i = None
        self.isEnd = False

# write cat
# make a trie for cat
word = 'cat'

# construction
head = Node(word[0])
curr = head