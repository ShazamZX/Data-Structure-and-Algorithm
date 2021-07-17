#Cycle in directed graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def cycle(self):
        visited = set()
        stack = {node:False for node in self.graph}
        def isCycle(node):
            nonlocal visited
            nonlocal stack
            visited.add(node)
            stack[node] = True
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if isCycle(neighbor) is True:
                        return True
                elif stack[neighbor] is True:
                    return True
            stack[node] = False
            return False

        for i in self.graph:
            if i not in visited:
                if isCycle(i) is True:
                    return True
        return False

#driver code

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.cycle() is True:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
