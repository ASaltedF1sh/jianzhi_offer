class ConnectingGraph:

    def __init__(self, n):
        self.boss = [0 for _ in range(n+1)]
        for i in range(1, n + 1):
            self.boss[i] = i
    
    def connect(self, a, b):
        c = self.find(a)
        d = self.find(b)
        if c != d:
            self.boss[d] = c

    def query(self, a, b):
        c = self.find(a)
        d = self.find(b)
        return c == d

    def find(self, a):
        if self.boss[a] == a:
            return a
        else:
            return self.find(self.boss[a])
