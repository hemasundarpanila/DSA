class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            cl=intervals[i]
            if res[-1][1]<cl[0]:
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1],cl[1])
        return res