'''You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
'''

'''BFS Solution This is similar to surrounded regions 1 extra step'''

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1) and grid[i][j]==1:
                    grid[i][j] = 2
                    queue.append((i,j))
        
        while queue:
            x,y = queue.pop(0)
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                r = x+dx
                c = y+dy
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                    grid[r][c]=2
                    queue.append((r,c))

        enclaves = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    enclaves+=1
        return enclaves



        