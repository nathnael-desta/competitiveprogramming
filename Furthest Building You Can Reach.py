class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        jumps = []
        for i in range(len(heights) - 1):
            h = heights[i + 1] - heights[i]
            if h <= 0: continue 
            heapq.heappush(jumps, h)

            if len(jumps) > ladders:
                bricks -= heapq.heappop(jumps)
            if bricks < 0:
                return i
        return len(heights) - 1