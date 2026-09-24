from collections import deque
class Solution:
    print("1" == True)
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]):
                    # dfs pour mettre toute l'ile a 0
                    stack = deque()
                    stack.append( (i,j) )
                    grid[i][j] = '0'
                    
                    while stack:
                        (y,x) = stack.pop()
                        
                        for dy, dx in [(0,-1),(-1,0), (0,1), (1,0)]:
                            #y correspond a i et x a j
                            if x+dx >=0 and x+dx < len(grid[0]) and y+dy >=0 and y+dy < len(grid):
                                if int(grid[y+dy][x+dx]):
                                    stack.append([y+dy, x+dx])
                                    grid[y+dy][x+dx]= '0'


                    num+= 1
        return num                    
