class UnionFind:
    
    def __init__(self, grid):
        self.height = len(grid)
        self.width = len(grid[0])
        self.boss = [-1 for _ in range(self.height * self.width)]
        self.block_count = 0

        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == '1':
                    self.boss[i * self.width + j] = i * self.width + j
                    self.block_count += 1

    #路径压缩
    def find(self, i):
        if self.boss[i] != i:
            self.boss[i] = self.find(self.boss[i])
        return self.boss[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        # print(root_x, root_y)
        if root_x != root_y:
            self.boss[root_y] = root_x
            self.block_count -= 1

    def getCount(self):
        return self.block_count

class Solution:

    def numIslands(self, grid):
        height = len(grid)
        if not height:
            return 0
        width = len(grid[0])

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        unionfind = UnionFind(grid)
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1':
                    grid[y][x] = '0'
                    for k in range(4):
                        h = dy[k] + y
                        w = dx[k] + x
                        if 0 <= h < height and 0 <= w < width and grid[h][w] == '1':
                            unionfind.union(y * width + x, h * width + w)

        return unionfind.getCount()
        

class Solution1:

    def BFS(self, grid):

        height = len(grid)
        if not height:
            return 0
        width = len(grid[0])

        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]

        block_count = 0
        queue = []

        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    queue.append([i, j])
                    while queue != []:
                        cur_land = queue[0]
                        grid[cur_land[0]][cur_land[1]] = '0'
                        queue.pop(0)
                        for k in range(4):
                            h = cur_land[0] + dh[k]
                            w = cur_land[1] + dw[k]
                            if 0 <= h < height and 0 <= w < width and grid[h][w] == '1':
                                queue.append([h, w])
                                grid[h][w] = '0'
                    block_count += 1
        return block_count
