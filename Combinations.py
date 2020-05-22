#回溯法，可以通过剪枝进一步优化效率
class Solution:
    def combine(self, n, k):
        self.ans = []
        choice = [i for i in range(1, n + 1)]
        self.helper(choice, [], k)
        return self.ans

    def helper(self, chs, res, k):
        if k == 0:
            self.ans.append(res)
            return

        for i in range(len(chs)):
            self.helper(chs[i + 1: ], res + [chs[i]], k - 1)
            
#剪枝：用时从500+ms变为十分之一
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        choice = [i for i in range(1, n + 1)]
        self.helper(choice, [], k)
        return self.ans

    def helper(self, chs, res, k):
        if k == 0:
            self.ans.append(res)
            return
        for i in range(len(chs)):
            #剪枝：这里通过一个判断，使无肯定法成型的枝减去
            #如果候选项的长度比需要的长度还短，则不必进入该分支
            if len(chs[i + 1: ]) >= k - 1:
                self.helper(chs[i + 1: ], res + [chs[i]], k - 1)
