#Breadth First Traversal

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,src):
        res = []
        visited = {node:False for node in self.graph}
        queue = []
        queue.append(src)
        visited[src] = True
        while queue:
            node = queue.pop(0)
            res.append(node) 
            """
            for searching a node n replace
            res.append(node) to ->
            if node == n:
                return True
            and instead of return res -> return False as default
            """
            for i in self.graph[node]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True
        return res


    #driver code

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
res = g.bfs(2)
print(*res)