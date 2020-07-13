# LintCode 919. 会议室 II

# 给定一系列的会议时间间隔intervals，包括起始和结束时间[[s1,e1],[s2,e2],...] (si < ei)，找到所需的最小的会议室数量。

# 样例1
# 输入: intervals = [(0,30),(5,10),(15,20)]
# 输出: 2
# 解释:
# 需要两个会议室
# 会议室1:(0,30)
# 会议室2:(5,10),(15,20)

# 样例2
# 输入: intervals = [(2,7)]
# 输出: 1
# 解释:
# 只需要1个会议室就够了


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
    @return: the minimum number of conference rooms required
    """

    #经典差分法，用字典进行优化，大大节省空间，不过需要一次排序，时间复杂度由ON变为OlogN
    def minMeetingRooms(self, intervals):
        if not intervals:
            return True
        from collections import defaultdict
        res = defaultdict(int)
        for time in intervals:
            res[time.start] += 1
            res[time.end] -= 1

        tmp = 0
        for i in sorted(res.keys()):
            tmp += res[i]
            #tmp大于1代表当前时段会议多于1个，返回False
            min_ = max(min_, tmp)
        return min_


    # 最小堆法
    # 按照开始时间对会议进行排序。
    # 初始化一个新的最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
    # 对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲。
    # 若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
    # 若房间不空闲。开新房间，并加入到堆中。
    # 处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数。

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        import heapq
        intervals.sort(key = lambda x: x[0])
        free_rooms = []
        #将第一个会议的结束时间放入堆中
        heapq.heappush(free_rooms, intervals[0][1])
        for interval in intervals[1::]:
            #检查堆顶房间是否空闲(即最早开的会议是不是在当前会议开始前就结束了)
            #如果空闲
            if free_rooms[0] <= interval[0]:
                #直接把该空闲房间分配给当前会议，因此时间需要更新，出堆再将当前会议结束时间加入堆中
                heapq.heappop(free_rooms)
            #如果不空闲，就直接开个新房间，新房间结束时间就是当前会议的结束时间
            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)


    # 扫描线法 + sort
    # 扫描线要点
    # 将起点和终点打散排序
    # 想象有个塔台，观察某个机场。机场的飞机一定是从机场飞出，再回到机场降落
    # 塔台上的人可以观察飞机起降，飞机起飞他就计数+1，飞机降落他就计数-1，
    # 由此一定可以算出来天上同时有多少架飞机正在飞行
    # [[1,3], [2,4]] => [[1,start],[2,start],[3,end],[4,end]]
    # 这个打散了再排序的过程实际上就是把飞机起降时间表转化为单个的起降事件
    # 而不用不去关心对于某个飞机的状态
    def minMeetingRooms(self, intervals):
        points = []
        for inv in intervals:
            points.append((inv.start, 1))
            points.append((inv.end, -1))
            
        points = sorted(points)
        cnt, res = 0, 0 
        for _, mark in points:
            cnt += mark
            res = max(res, cnt)
        return res
              
