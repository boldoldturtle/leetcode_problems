class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)

    def adjacentSum(self, value: int) -> int:
        for i in range(self.n):
          for j in range(self.n):
            if self.grid[i][j] == value:
              res = 0
              if j-1 >= 0:
                res += self.grid[i][j-1]
              if j+1 < self.n:
                res += self.grid[i][j+1]
              if i+1 < self.n:
                res += self.grid[i+1][j]
              if i-1 >= 0:
                res += self.grid[i-1][j]
              return res

    def diagonalSum(self, value: int) -> int:
        for i in range(self.n):
          for j in range(self.n):
            if self.grid[i][j] == value:
              res = 0
              if i+1 < self.n and j+1 < self.n:
                res += self.grid[i+1][j+1]
              if i+1 < self.n and j-1 >= 0:
                res += self.grid[i+1][j-1]
              if i-1 >= 0 and j+1 < self.n:
                res += self.grid[i-1][j+1]
              if i-1 >= 0 and j-1 >= 0:
                res += self.grid[i-1][j-1]
              return res
              
