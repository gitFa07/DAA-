class DirectedGraph:
    def __init__(self):
        self.graph = {} # Adjacency list, disctionary {"": ["", "", ...]}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = [] # e.g. "A" -> {"A": []}

    def add_edge(self, u, v):
        # one direction only
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.graph[u]:
            self.graph[u].append(v)
        
    def delete_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

    def search_edge(self, u, v):
        return u in self.graph and v in self.graph[u]

    def show(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

g= DirectedGraph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("C", "D")
g.add_edge("D", "A")


g.show()
