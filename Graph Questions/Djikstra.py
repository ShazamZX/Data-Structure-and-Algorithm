#Implement Djikstra's algo to find shortest path (GREEDY APPROACH using Priority Queue)
import heapq
from collections import defaultdict
class Edge:
    def __init__(self,node,wt):
        self.node = node
        self.wt = wt
    def __lt__(self,next):
        return self.wt < next.wt
    

def shortest_path(src,des,graph):
    pq = []
    path = []
    visited = set()
    visited.add(src)
    heapq.heappush(pq,Edge(src,0))
    while pq:
        curr = heapq.heappop(pq)
        path.append(curr.node)
        if curr.node == des:
            print(*path, sep="-->")
            print(curr.wt)
            return
        for neighbor in graph[curr.node]:
            if neighbor.node not in visited:
                heapq.heappush(pq,Edge(neighbor.node,curr.wt+neighbor.wt))
                visited.add(neighbor.node)
    print("No Path Exists")
    return


#driver code

graph = defaultdict(list)


graph[0].append(Edge(1, 9));
graph[0].append(Edge(2, 6));
graph[0].append(Edge(3, 5));
graph[0].append(Edge(4, 3));

graph[2].append(Edge(1, 2));
graph[2].append(Edge(3, 4));

shortest_path(1,3,graph)






