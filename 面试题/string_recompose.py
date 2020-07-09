    def string_subset(self, s):
        ans = []
        def helper(res, tmp):
            if tmp:
                ans.append(tmp)
            for k in range(len(res)):
                helper(res[k + 1: ], tmp + [res[k]])
        helper(s, [])
        return ans
