#Cycle in undirected graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def cycle(self):
        visited = set()
        def isCycle(node,parent):
            nonlocal visited
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if isCycle(neighbor,node) is True:
                        return True
                elif neighbor!=parent:
                    return True
            return False

        for i in self.graph:
            if i not in visited:
                if isCycle(i,None) is True:
                    return True
        return False

#driver code

g = Graph()
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
if g.cycle():
    print("Graph contains cycle")
else :
    print("Graph does not contain cycle ")
g1 = Graph()
g1.addEdge(0,1)
g1.addEdge(1,2)
 
 
if g1.cycle():
    print("Graph contains cycle")
else :
    print("Graph does not contain cycle ")
