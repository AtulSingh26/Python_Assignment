def dfs(grid , i,j,n,m):
        if i<0 or j<0 or i>=n or j>=m or grid[i][j]==2 or grid[i][j]==1:
            return 0

        grid[i][j] =2

        a= dfs(grid, i+1, j, n, m)
        b= dfs(grid, i-1, j, n, m)
        c=dfs(grid, i, j+1, n, m)
        d=dfs(grid, i, j-1, n, m)
        return 1+a+b+c+d


def max_path(grid):
    n= len(grid)
    m= len(grid[0])
    ans =0

    for i in range(n):
        for j in range(m):
            if(grid[i][j]==0):
                ans = max(ans,dfs(grid,i,j,n,m))


    return ans

lst = [[1,0,0,0,1]]

print(max_path(lst))







