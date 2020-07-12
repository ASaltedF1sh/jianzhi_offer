class Solution:
    def reverse(self, s):
        def get_last_item(s):
            tmp = s.pop()
            if not s:
                return tmp
            last = get_last_item(s)
            s.append(tmp)
            return last

        if not len(s):
            return
        #获得栈尾元素
        last = get_last_item(s)
        if not last:
            return
        #递归
        self.reverse(s)
        s.append(last)

if __name__ == '__main__':
    a = list('abcdef')
    Solution().reverse(a)
    print(a)
