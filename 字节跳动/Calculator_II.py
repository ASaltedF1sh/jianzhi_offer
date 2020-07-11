#递归解法
class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque
        def helper(s):
            op, num = '+', 0
            stack = []

            #这里需要从左边不断剔除元素，才能正常完成递归
            while len(s) > 0:
                ch = s.popleft()
                if ch.isdigit():
                    num = 10 * num + int(ch)
                if ch == '(':
                    num = helper(s)

                #本次遇到运算符号或者到达末尾，才会处理上次的运算,然后暂时保存本次的运算符
                if (not ch.isdigit() and ch != ' ') or len(s) == 0:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    elif op == '/':
                        stack.append(int(stack.pop() / num))
                    num, op = 0, ch
                # 遇到右括号返回递归结果
                if ch == ')':
                    break
            return sum(stack)
        return helper(deque(s))

#栈解法（不适用于有乘除）
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0       # For the on-going result
        sign = 1      # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)

            elif ch == '+':
                res += sign * operand        
                sign = 1
                operand = 0

            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif ch == ')':
                res += sign * operand
                res *= stack.pop() # stack pop 1, sign
                res += stack.pop() # stack pop 2, operand
                operand = 0

        return res + sign * operand
