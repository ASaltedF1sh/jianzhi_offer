class ConnectingGraph2:

    def __init__(self, n):
        self.boss = [0 for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

        for i in range(1, n + 1):
            self.boss[i] = i
    
    def connect(self, a, b):
        c = self.find(a)
        d = self.find(b)
        if c != d:
            self.boss[d] = c
            self.size[c] += self.size[d]



    def query(self, a):
        return self.size[self.find(a)]

    def find(self, a):
        if self.boss[a] == a:
            return a
        else:
            #一直找到最顶层的老大
            return self.find(self.boss[a])
