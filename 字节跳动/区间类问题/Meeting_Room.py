# LintCode 920. 会议室

# 给定一系列的会议时间间隔，包括起始和结束时间[[s1,e1]，[s2,e2]，…(si < ei)，确定一个人是否可以参加所有会议。

# 样例1
# 输入: intervals = [(0,30),(5,10),(15,20)]
# 输出: false
# 解释:
# (0,30), (5,10) 和 (0,30),(15,20) 这两对会议会冲突

# 样例2
# 输入: intervals = [(5,8),(9,15)]
# 输出: true
# 解释:
# 这两个时间段不会冲突
# 注意事项
# (0,8),(8,10)在8这这一时刻不冲突



"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    #差分解法
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        res = [0] * 2000000
        for time in intervals:
            res[time.start] += 1
            res[time.end] -= 1

        tmp = 0
        for i in res:
            tmp += i
            #tmp大于1代表当前时段会议多于1个，返回False
            if tmp > 1:
                return False 
        return True

    #排序解法
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda x: x.start)
        for i in range(1, len(intervals)):
            #一个会议开始时，上一个开始的会议必须已经结束
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True
