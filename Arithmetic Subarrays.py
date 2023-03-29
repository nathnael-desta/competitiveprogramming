class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        newarr = []
        res = []
        for i in range(len(l)):
            value = True
            newarr = nums[l[i]:r[i] + 1]
            heapq.heapify(newarr)
            x = heapq.heappop(newarr)

            if len(newarr) >= 1:
                y = heapq.heappop(newarr)
                d = y - x
                count = 2
                while len(newarr) != 0:
                    z = heapq.heappop(newarr)
                    if (z - x != d * count):
                        value = False
                    count += 1
                    if value != True:
                        break
            else:
                value = False
            res.append(value)
        return res