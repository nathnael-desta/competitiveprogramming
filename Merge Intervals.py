class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        new = [intervals[0]]

        for s, e in intervals:
            if s <= new[-1][1]:
                ending = new[-1][1]
                new[-1][1] = max(ending, e)
            else:
                new.append([s,e])
        return new