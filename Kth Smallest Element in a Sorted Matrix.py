class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = []
        for i in matrix:
            for j in range(len(i)):
                arr.append(i[j])
        heapq.heapify(arr)
        res = 0
        for i in range(k):
            res = heapq.heappop(arr)
        return res