import heapq

class Solution(object):
    def kClosest(self, points, k):  # points = [[3,3],[5,-1],[-2,4]] k = 2
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y]) 
        # [[18, 3, 3], [26, 5, -1], [20, -2, 4]]

        heapq.heapify(minHeap)  # heapq is the built in module
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res  # [[3,3],[-2,4]]
