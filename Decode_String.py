# 递归
class Solution:
    def decodeString(self, s: str) -> str:

        def helper(tmp):
            if  tmp == '':
                return tmp
            count_l = 0
            count_r = 0
            l_ind = 0
            r_ind = 0
            num = 0
            num_continue = True

            for i in range(len(tmp)):
                if tmp[i] == '[':
                    count_l += 1
                    num_continue = False
                    if not l_ind:
                        l_ind = i

                elif tmp[i] == ']':
                    count_r += 1
                    r_ind = i
                    if count_l == count_r:
                        return helper(tmp[l_ind + 1 : r_ind]) * num + helper(tmp[r_ind + 1:])

                elif tmp[i].isdigit():
                    if not num:
                        num = int(tmp[i])
                        continue
                    if num and num_continue:
                        num = 10 * num + int(tmp[i])

                else:
                    if not count_l:
                        return tmp[i] + helper(tmp[i+1:])

        return helper(s)
        
#栈
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res

#正则
class Solution:
    def decodeString(self, s: str) -> str:
        import re
        def f(m):
            return int(m.group(1))* m.group(2)
        while '[' in s:
            s = re.sub(r'(\d+)\[([A-Za-z]*)\]', f, s)
        return s
