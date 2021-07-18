"""
Given a Directed Acyclic Graph having V vertices and E edges, where each edge {U, V} represents the Jobs U and V such that Job V can only be started only after completion of Job U. The task is to determine the minimum time taken by each job to be completed where each Job takes unit time to get completed.
"""


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.inorder = defaultdict(int)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.inorder[v]+=1

    def jobtime(self):
        queue = []
        time = dict.fromkeys(self.graph.keys(),0)
        for i in list(self.graph.keys()):
            if self.inorder[i] == 0:
                time[i] =1
                queue.append(i)
        
        while(queue):
            job = queue.pop(0)
            for i in self.graph[job]:
                self.inorder[i]-=1
                if self.inorder[i] == 0:
                    time[i] = time[job]+1
                    queue.append(i)
        return time


#driver


g = Graph()

g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 6)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 10)

print(g.jobtime())

