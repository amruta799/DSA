'''There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
'''


'''
This is a simple implementation dfs (Convert 2d array to graph and apply bfs or dfs)
'''
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.create_graph(isConnected)
        vis = [0 for i in range(len(graph)+1)]
        c = 0
        for node in graph:
            if not vis[node]:
                self.dfs(node,vis,graph)
                c+=1
        return c
    
    def dfs(self,i,vis,graph):
        vis[i]=1
        for node in graph[i]:
            if not vis[node]:
                self.dfs(node,vis,graph)

    def create_graph(self,isConnected):
        graph = {}
        for i in range(1,len(isConnected)+1):
            graph[i] = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        return graph
        

            


        
        
    
        