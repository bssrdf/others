# amazon

class Solution:
    def findPath(self, maze):
        visited = [[0 for i in range(len(maze[0]))] for j in range(len(maze))]
        self.findPathRecur(maze, visited, 0, 0)
        return visited
        
    def findPathRecur(self, maze, visited, i, j):
        if i == len(maze)-1 and j == len(maze[0])-1 and maze[i][j] == 0: 
            visited[-1][-1] = 1; return True
        if i <0 or i >= len(maze): return False
        if j <0 or j >= len(maze[0]): return False
        if maze[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            if (self.findPathRecur(maze, visited, i+1, j) or self.findPathRecur(maze, visited, i-1, j) or self.findPathRecur(maze, visited, i, j+1) or self.findPathRecur(maze, visited, i, j-1)) is False:
                visited[i][j] = 0; return False
            else:
                return True
        return False

if __name__ == "__main__":
    maze = [[0,1,1,1],
            [0,0,1,0],
            [1,0,1,1],
            [1,0,0,0]]
    s = Solution()
    sol = s.findPath(maze)
    for line in sol:
        print line
