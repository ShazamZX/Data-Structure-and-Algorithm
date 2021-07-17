from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,src):
        visited = set()
        res = []
        def dfs_helper(src,visited):
            nonlocal res
            visited.add(src)
            res.append(src)
            for neighbour in self.graph[src]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs_helper(neighbour,visited)
        
        dfs_helper(src,visited)
        print(*res)
    

    #driver code

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.dfs(2)
