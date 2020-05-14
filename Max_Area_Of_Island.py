class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        if not height:
            return 0
        width = len(grid[0])

        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]

        max_area = 0
        queue = []

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    area = 0
                    while queue != []:
                        cur_land = queue[0]
                        grid[cur_land[0]][cur_land[1]] = 0
                        queue.pop(0)
                        area += 1
                        for k in range(4):
                            h = cur_land[0] + dh[k]
                            w = cur_land[1] + dw[k]
                            if 0 <= h < height and 0 <= w < width and grid[h][w] == 1:
                                queue.append([h, w])
                                grid[h][w] = 0
                    max_area = max(max_area, area)
        return max_area
