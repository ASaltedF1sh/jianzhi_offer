#双队列实现
class MyStack:
    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def push(self, x):
        self.in_queue.append(x)

    def pop(self):
        while len(self.in_queue) > 1:
            self.out_queue.append(self.in_queue.popleft())
        self.in_queue, self.out_queue = self.out_queue, self.in_queue
        return self.out_queue.popleft()

    def top(self):
        while len(self.in_queue) > 1:
            self.out_queue.append(self.in_queue.popleft())
        ans = self.in_queue.popleft()
        self.out_queue.append(ans)
        self.in_queue, self.out_queue = self.out_queue, self.in_queue
        return ans

    def empty(self):
        return not self.in_queue
        
  
  #单个队列实现
  
  class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        tmp = len(self.queue) - 1
        while tmp:
            self.queue.append(self.queue.popleft())
            tmp -= 1
        return self.queue.popleft()

    def top(self):
        tmp = len(self.queue) - 1
        while tmp:
            self.queue.append(self.queue.popleft())
            tmp -= 1
        ans = self.queue.popleft()
        self.queue.append(ans)
        return ans

    def empty(self):
        return not self.queue
