'''There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
'''

'''BFS solution: The key to solve this question is to do either bfs or dfs traversal along with that
Assign alternate colors to the nodes if the node is not colored, if the node is colored and color is 
same as it's source node color the return false , there can be multile component graphs so use for loop
for making dfs and bfs call'''

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d_graph = self.create_graph(graph)
        color = [-1 for i in range(len(d_graph))]
        col = 0
        for i in range(len(d_graph)):
            if color[i] == -1:
                if self.bfs(d_graph,i,color,col)==False:
                    return False
        return True
    
    def bfs(self,d_graph,source,color,col):
        queue = []
        queue.append(source)
        color[source] = col
        while queue:
            source = queue.pop(0)
            for i in d_graph[source]:
                if color[i] == -1:
                    color[i] = not color[source]
                    queue.append(i)
                elif color[i]==color[source]:
                    return False
        return True
    
    def create_graph(self,graph):
        d_graph = {}
        for i in range(len(graph)):
            if i not in d_graph.keys():
                d_graph[i] = []
        for i in range(len(graph)):
            d_graph[i].extend(graph[i])
        return d_graph
    
'''DFS Solution'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d_graph = self.create_graph(graph)
        color = [-1 for i in range(len(d_graph))]
        col = 0
        for i in range(len(d_graph)):
            if color[i]==-1:
                if self.dfs(i,color,d_graph,col)==False:
                    return False
        return True
    
    def dfs(self,source,color,d_graph,col):
        color[source] = col
        for i in d_graph[source]:
            if color[i]==-1:
                if self.dfs(i,color,d_graph, not col)==False:
                    return False
            elif color[i]==color[source]:
                return False
        return True


    def create_graph(self,graph):
        d_graph = {}
        for i in range(len(graph)):
            if i not in d_graph.keys():
                d_graph[i] = []
        for i in range(len(graph)):
            d_graph[i].extend(graph[i])
        return d_graph
        
    
                       