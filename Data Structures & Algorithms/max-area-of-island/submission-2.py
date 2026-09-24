from collections import deque
class Solution:

    def dfs(self, graph, node):

        stack = deque()
        visited = []

        stack.append(node)
        visited.append(node)
        while stack:
            s = stack.pop()

            for n in graph[s]:
                if n not in visited:
                    stack.append(n)
                    visited.append(n)
        return visited



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                """if j>1 and grid[i][j] ==1 and (i,j-1) in dic:
                    dic[(i,j)] = dic[(i,j-1)] + 1
                elif i>1 and grid[i][j] ==1 and (i-1,j) in dic:
                    dic[(i,j)] = dic[(i-1,j)] + 1
                elif grid[i][j] ==1:
                    dic[(i,j)] = 1"""
                if grid[i][j] ==1:
                    area = 0
                    stack = deque([(i,j)])
                    grid[i][j] = 0

                    while stack:
                        s = stack.pop()
                        area+=1
                        for d in [(s[0]-1,s[1]),(s[0],s[1]-1),(s[0],s[1]+1),(s[0]+1,s[1])]:
                            if d[0]>=0 and d[0]<len(grid) and d[1]>=0 and d[1]<len(grid[0]):
                                #la direction est valid
                                if grid[d[0]][d[1]] == 1:
                                    stack.append( (d[0] , d[1]) )
                                    grid[d[0]][ d[1]] = 0
                    maxArea = max(maxArea, area)
        
        return maxArea




                    
