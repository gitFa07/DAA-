
from collections import deque

class UndirectedGraph: 
    def __init__(self): # constructor of this class so we can make objects of this class, have multiple graphs
        self.graph = {} # Adjacency list, disctionary {"": ["", "", ...]}

    def add_vertex(self, v):
        if v not in self.graph: # if vertex is not in graph, add it
            self.graph[v] = [] # e.g. "A" -> {"A": []}

    def add_edge(self, u, v):
        # add both ways for undirected graph
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def delete_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def search_edge(self, v, u):
        return u in self.graph and v in self.graph[u]

    def show(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def bfs(self, start):
        if start not in self.graph:
            return []
        visited = set([start])
        q = deque([start])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nb in self.graph[node]:
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        return 
    
    def dfs_recursive(self, start):
        if start not in self.graph:
            return []
        visited = set()
        order = []
        def dfs(u):
            visited.add(u)
            order.append(u)
            for nb in self.graph[u]:
                if nb not in visited:
                    dfs(nb)
        dfs(start)
        return order

ug = UndirectedGraph()
ug.add_edge("A", "B")
ug.add_edge("A", "C")
ug.add_edge("B", "D")

print(ug.bfs("A"))
print(ug.dfs_recursive("A"))
ug.show()
