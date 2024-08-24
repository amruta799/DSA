'''You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]'''


'''BFS Solution: The main key to solve this problem is to replace edge cells that contains "O" 
with some other variable and apply bfs only on those indexes so that every "O"
will be replced and finally replace that variable with "O" and remaining "O" with "X"'''


from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_len = len(board)
        col_len = len(board[0])
        queue= []
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j]=='O' and (i==0 or j==0 or i==row_len-1 or j==col_len-1):
                    queue.append((i,j))
                    board[i][j] = "A"

        while len(queue):
            x,y = queue.pop(0)
            for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
                r = x+i
                c = y+j
                if 0<=r<row_len and 0<=c<col_len and board[r][c] == "O":
                    board[r][c] = "A"
                    queue.append((r,c))
        
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == "O":
                    board[i][j] = 'X'


'''DFS Solution same logic'''

class Solution:

 def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board=board
        n=len(board)
        m=len(board[0])
        if(n<=2):
            return
        if(m<=2):
            return
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O' and (i==0 or j==0 or i==n-1 or j==m-1):
                    self.dfs(i,j)
                    
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O': 
                     self.board[i][j]='X'
                elif(self.board[i][j]=='A'): 
                    self.board[i][j]='O'          
    
def dfs(self,i,j):
    if i>=0 and j>=0 and i<len(self.board) and j<len(self.board[0])  and self.board[i][j]=='O':
        self.board[i][j]='A'
        self.dfs(i,j+1)
        self.dfs(i,j-1)
        self.dfs(i+1,j)
        self.dfs(i-1,j)

        

        
        
        