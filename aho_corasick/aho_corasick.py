from collections import deque, defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.output = set()
        self.fail = None


class AhoCorasick:
    def __init__(self, strings: List[str]):
        self.root = TrieNode()
        self.build_trie(strings)
        self.build_fail()

    def build_trie(self, strings: List[str]):
        for s in strings:
            curr = self.root
            for c in s:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.output.add(s)

    def build_fail(self):
        q = deque([self.root])
        while q:
            curr_node = q.popleft()
            for n, node in list(curr_node.children.items()):
                if curr_node is self.root:
                    node.fail = curr_node
                else:
                    p = curr_node.fail
                    while p is not self.root and n not in p.children:
                        p = p.fail
                    if n in p.children:
                        p = p.children[n]
                    node.fail = p
                    node.output.update(p.output)
                q.append(node)


def multi_string_search(long_string: str, dictionary: List[str]) -> List[bool]:
    ac = AhoCorasick(dictionary)

    matches = defaultdict(list)
    curr_node = ac.root

    for i in range(len(long_string)):
        letter = long_string[i]

        while curr_node is not ac.root and letter not in curr_node.children:
            curr_node = curr_node.fail
        if letter in curr_node.children:
            curr_node = curr_node.children[letter]

        for w in curr_node.output:
            # start index in long string for which a dictionary word was found
            matches[w].append(i - len(w) + 1)

    return [s in matches for s in dictionary]


if __name__ == "__main__":
    long_string = "ATCGGGCTATCGGGGACTGGTACCCAAAAACTGGGGGGGCACGTTTTGA"
    dictionary = ["ATGGA", "GGACT", "GGGG", "AAACT", "ACTG"]
    res = multi_string_search(long_string, dictionary)
    print(res)
