class ConnectingGraph3:

    def __init__(self, n):
        self.boss = [0 for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.block = n

        for i in range(1, n + 1):
            self.boss[i] = i
    
    def connect(self, a, b):
        c = self.find(a)
        d = self.find(b)
        if c != d:
            self.boss[d] = c
            self.size[c] += self.size[d]
            self.block -= 1

    def query(self):
        return self.block

    def find(self, a):
        if self.boss[a] == a:
            return a
        else:
            return self.find(self.boss[a])
