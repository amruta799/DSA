'''An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

 '''

''' DFS Solution: Here we modify the given matrix to new color so the key is to
store initial value in some variable and then apply dfs from the position for source
in all four direction and keep replacing value to new color if the value is equal to 
source initially
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        source = image[sr][sc]
        if image[sr][sc]==newColor:
            return image
        self.dfs(source,image,sr,sc,newColor)
        return image

    def dfs(self,source,image,i,j,newColor):
        if i<0 or i>=len(image) or j<0 or j>=len(image[0]):
            return
        if image[i][j] != source:
            return
        image[i][j]=newColor
        self.dfs(source,image,i-1,j,newColor)
        self.dfs(source,image,i+1,j,newColor)
        self.dfs(source,image,i,j-1,newColor)
        self.dfs(source,image,i,j+1,newColor)

'''BFS Solution:
In this bfs traversal the main key is to store the source value initially
and traverse to its neighbours and replace it with new color if initial value is 
source
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [[sr, sc]]
        visited = set()
        source = image[sr][sc]
        row_size = len(image)
        col_size = len(image[0])
        image[sr][sc] = newColor
        while len(queue) > 0:
            print(queue)
            x, y = queue.pop(0)
            r_c_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            pos = str(x) + "," + str(y)
            
            if pos not in visited:
                visited.add(pos)
                for row, col in r_c_delta:
                    r = x + row
                    c = y + col
                    if (0 <= r < row_size) and (0 <= c < col_size) and image[r][c] == source:
                        image[r][c] = newColor
                        queue.append([r, c])
        
        return image
