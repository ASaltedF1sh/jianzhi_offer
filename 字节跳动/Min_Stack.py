# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        #如果要入栈的元素是新的最小值，则把原来的最小值先入栈，在将新元素入栈
        #注意：等于的时候也应该将当前最小值入栈，否则pop的时候会出错
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        #如果出栈的元素是当前的最小值，那么需要再出栈一次，得到之前的保存的前最小值
        if self.min == self.stack.pop():
            self.min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
