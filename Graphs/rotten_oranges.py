'''You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.'''

# BFS (Solution)
'''The preffered solution for this question is BFS Since it inclued traversing all the neighbours first,
Key approach is to apply bfs on the neighbours of rotten oranges and append those indecies back to the 
queue while incrementing the minutes count'''


from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            indexs = deque()
            fresh = 0
            minutes = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==2:
                        indexs.append((i,j))
                    elif grid[i][j]==1:
                        fresh += 1
            while indexs and fresh>0:
                minutes = minutes+1
                for k in range(len(indexs)):
                    i,j = indexs.popleft()
                    for row,column in [[0,1],[0,-1],[1,0],[-1,0]]:
                        x = i+row
                        y = j+column
                        if len(grid)>x>=0 and len(grid[0])>y>=0 and grid[x][y]==1:
                            fresh -= 1
                            grid[x][y] = 2
                            indexs.append((x,y))

            if fresh == 0:
                return minutes
            else:
                return -1 

#  DFS (Solution)
'''This solution is bit tricky since the dfs is applied the value can be over written
so the edge case should be carefully included also answer max value of grid -2 since
we are considering initial value as 2'''

class Solution:
    def processGrid(self, grid, r, c,minutes):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0 or (grid[r][c]>1 and grid[r][c]<minutes):
                return
            grid[r][c]=minutes
            self.processGrid(grid, r - 1, c,minutes+1)
            self.processGrid(grid, r + 1, c,minutes+1)
            self.processGrid(grid, r, c - 1,minutes+1)
            self.processGrid(grid, r, c + 1,minutes+1)
    

    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    self.processGrid(grid, r, c,minutes)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
                minutes = max(minutes,grid[r][c])
            
        return minutes-2
                    

