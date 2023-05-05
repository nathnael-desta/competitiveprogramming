class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        count = 0
        res = 0
        for i in nums:
            arr.append(i)
            if i == 0:
                count += 1
            if count == 2:
                while True:
                    if arr.pop(0) != 1:
                        break
                count -= 1
            res = max(res, len(arr) - 1)

        return res


rand = Solution()
print(rand.longestSubarray([1,1,1]))