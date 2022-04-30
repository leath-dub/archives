#!/usr/bin/env python3

import sys

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFSPaths(object):

    def __init__(self, g, s):
       self.g = g
       self.s = s
       self.visited = [False for _ in range(g.V)]
       self.parent = [False for _ in range(g.V)]
       self.dfs(s)

    def dfs(self, v):
       self.visited[v] = True
       for w in self.g.adj[v]:
          if not self.visited[w]:
             self.parent[w] = v
             self.dfs(w)


def main() -> None:
    V = int(input())
    graph = Graph(V)
    for vw in sys.stdin:
        vw = vw.strip().split()
        v = int(vw[0])
        w = int(vw[1])
        graph.addEdge(v, w)

    islands = 0
    paths = DFSPaths(graph, 0)
    while False in paths.visited:
        i = paths.visited.index(False)
        paths.dfs(i)
        islands += 1
    print(islands + 1)


if __name__ == "__main__":
    main()
