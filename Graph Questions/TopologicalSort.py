#Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    

    def topological_sort(self):
        stack = [] #storing elements in post order
        visited = set()
        
        for node in list(self.graph.keys()):
            if node not in visited:
                self.dfs(node,visited,stack)
        for i in range(len(stack)):
            print(stack.pop())

    def dfs(self,src,visited,stack):
        visited.add(src)
        for neighbor in self.graph[src]:
            if neighbor not in visited:
                self.dfs(neighbor,visited,stack)
        stack.append(src)
#driver

g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(g.graph)
g.topological_sort()