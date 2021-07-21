#Given an undirected graph and a number m, determine if the graph can be coloured with at most m colours such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. 
from collections import defaultdict
ans = 0
def isSafe(graph,colors,node,c):
    for neighbor in graph[node]:
        if colors[neighbor] == c:
            return False
    return True

def waystocolor_util(graph,nodes, colors,n,total_n,m_colors):
    # print(nodes[n])
    global ans
    if n == (total_n-1):
        ans+=1
        # print(ans)
        return
    for i in range(m_colors):
        if isSafe(graph,colors,nodes[n],i):
            colors[nodes[n]] = i
            waystocolor_util(graph,nodes, colors,(n+1),total_n,m_colors)
            colors[nodes[n]] = None
    return 

def waystocolor(graph,m_colors):
    global ans
    nodes = list(graph.keys())
    total_n = len(nodes)
    colors = dict.fromkeys(nodes)
    # ans = 0
    waystocolor_util(graph,nodes,colors,0,total_n,m_colors)
    print(ans)

#driver code

graph = {
    1:[2,3,4],
    2:[1,3],
    3:[1,2,4],
    4:[1,3]
}

waystocolor(graph,3)