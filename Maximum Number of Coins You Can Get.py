class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        res = 0
        count = int(len(piles) / 3)
        piles = [-x for x in piles]
        heapq.heapify(piles)
        while count > 0:
            heapq.heappop(piles)
            res += -heapq.heappop(piles)
            count -= 1
        return res