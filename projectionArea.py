class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0

        n = len(grid)

        area += n * n

        for row in grid:
            area += max(row)

        for cl in range(0, n):
            collum = []
            for row in grid:
                collum.append(row[cl])
            area += max(collum)

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    area -= 1

        return area