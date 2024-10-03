class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        dp = [[float('inf')] * col for _ in range(row)]
        dp[0] = grid[0]
        
        for i in range(1, row):
            for j in range(col):
                min_value = float('inf')
                for k in range(col):
                    if k != j:  
                        min_value = min(min_value, dp[i-1][k])
                
                dp[i][j] = grid[i][j] + min_value
        
        return min(dp[-1])
