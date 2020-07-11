# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
# 表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

# 示例 1:
# 输入: "3+2*2"
# 输出: 7

# 说明：
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。

#思路：一个栈，遍历一遍
# 1.遇到数字：入栈
# 2.遇到空格：跳过
# 3.遇到运算符，查找下一个数字num
#    a.遇到 '+' : num直接入栈
#    b.遇到 '-' : -num直接入栈
#    c.遇到 '*' : pop(-1) * num ,结果入栈
#    d.遇到 '/' : pop(-1) / num ,结果入栈
# 4.将栈中所有数字相加即可

class Solution:
    def calculate(self, s: str) -> int:

        num_set = list('0123456789')
        stack, op, num = [], '+', ''

        for i in range(len(s)):
            ch = s[i]
            if ch in num_set:
                num += ch

            #本次遇到运算符号或者到达末尾，才会处理上次的运算,然后暂时保存本次的运算符
            if (ch not in num_set and ch != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(int(num))
                elif op == '-':
                    stack.append(-int(num))
                elif op == '*':
                    stack.append(stack.pop() * int(num))
                else:
                    stack.append(int(stack.pop() / int(num)))
                num, op = '', ch

        ans = 0
        while stack:
            ans += stack.pop()
        return ans
