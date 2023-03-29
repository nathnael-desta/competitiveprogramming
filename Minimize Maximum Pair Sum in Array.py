class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev = [-x for x in nums]
        l = len(rev)
        heapq.heapify(rev)
        heapq.heapify(nums)
        sums = []
        while len(rev) != l / 2:
            x = -heapq.heappop(rev)
            y = heapq.heappop(nums)
            sums.append(x + y)
        return max(sums)