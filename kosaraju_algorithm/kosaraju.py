from typing import List


class Kosaraju:
    def __init__(self, n: int, edges: List[List[int]]):
        self.make_adjacency_lists(n, edges)
        self.n = n
        self.order_stack = []
        self.visited1 = set()
        self.visited2 = set()
        self.who = [0] * self.n

    def make_adjacency_lists(self, n: int, edges: List[List[int]]):
        self.adj = [[] for _ in range(n)]
        self.r_adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.r_adj[v].append(u)

    def find_sccs(self):
        for node in range(n):
            self.dfs1(node)

        while self.order_stack:
            curr = self.order_stack.pop()
            if curr in self.visited2:
                continue
            self.dfs2(curr, curr)
        return self.who

    def dfs1(self, node):
        if node in self.visited1:
            return

        self.visited1.add(node)
        for nei in self.adj[node]:
            self.dfs1(nei)

        self.order_stack.append(node)

    def dfs2(self, node, root):
        if node in self.visited2:
            return

        self.visited2.add(node)
        self.who[node] = root
        for nei in self.r_adj[node]:
            self.dfs2(nei, root)
