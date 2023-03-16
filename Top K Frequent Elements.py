class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 0
        for keys, values in dic.items():
            heap.append([values, keys])
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        ans = []
        for i in heap:
            ans.append(i[1])
        return ans