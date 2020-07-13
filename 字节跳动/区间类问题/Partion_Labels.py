# 763. 划分字母区间
# 难度
# 中等

# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

# 示例 1：
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

# 提示：
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。


#线扫描法，想象成机场问题，当天上最后一架飞机降落之际，就会产生一个要划分的区间了

class Solution:
    def partitionLabels(self, S):
        if not S:
            return
        dic = dict()
        for i in range(len(S)):
            if S[i] not in dic:
                dic[S[i]] = [i, -1]
            else:
                dic[S[i]][-1] = i

        #线扫描法经典做法，将起点和终点打散
        tmp = []
        for inv in dic.values():
            tmp.append((inv[0], 1))
            #这里的判断语句主要考虑到只出现一次的点，相当于该飞机在同一时刻起飞并降落（什么鬼 。。。）
            if inv[1] == -1:
                tmp.append((inv[0], -1))
            else:
                tmp.append((inv[1], -1))
        ans = []
        res = 0

        #这里排序除了要按时间节点之外，一定要把起飞排到降落之前
        for event in sorted(tmp, key = lambda x: (x[0], -x[1])):
            res += event[-1]
            if res == 0:
                ans.append(event[0])

        #ans保存的是每个区间最后一个字符的位置，因此还要处理后才能输出
        ans_ = [ans[0] + 1]
        for i in range(1, len(ans)):
            ans_.append(ans[i] - ans[i-1])
        return ans_
