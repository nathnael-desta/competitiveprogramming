class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-i for i in stones]
        heapq.heapify(stones)
        print(stones)
        if len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            res = s1 - s2
            if res != 0:
                heapq.heappush(stones, res)
            elif len(stones) == 0:
                stones.append(0)

        stones = [-i for i in stones]
        print(stones)
        if len(stones) == 1:
            return stones[0]
        return self.lastStoneWeight(stones)