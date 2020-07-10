class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # (rand7() - 1) * 7 :出现的数字为0, 7, 14, 28, 35, 42, 49
        #然后再来一个rand(7)，范围为1 ~ 7
        #则ans范围 1 ~ 49，每个数出现的可能性都一样
        while True:
            ans = (rand7() - 1) * 7 + rand7()
            #只保留范围1 ~ 40
            if ans > 40:
                continue
            #这样操作是为了把10,20，30,40转换为1，把9,19,29,39转换为10
            return ans % 10 + 1
