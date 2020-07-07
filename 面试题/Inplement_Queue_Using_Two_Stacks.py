class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        if self.out_stack:
            while self.out_stack:
                self.in_stack.append(self.out_stack.pop())
        self.in_stack.append(x)

    def pop(self):
        if self.in_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.in_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_queue or not self.out_stack
