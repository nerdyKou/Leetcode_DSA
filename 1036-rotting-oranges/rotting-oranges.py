class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        vis = [[0] * m for _ in range(n)]

        fresh = 0
        rotten = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    vis[i][j] = 2
                elif grid[i][j] == 1:
                    fresh += 1

        tm = 0

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        while q:
            r, c, t = q.popleft()

            tm = max(tm, t)

            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]

                if (0 <= nrow < n and
                    0 <= ncol < m and
                    vis[nrow][ncol] == 0 and
                    grid[nrow][ncol] == 1):

                    q.append((nrow, ncol, t + 1))
                    vis[nrow][ncol] = 2
                    rotten += 1

        if rotten != fresh:
            return -1

        return tm