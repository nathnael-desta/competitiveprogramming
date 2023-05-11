class Solution:
    def minSubArrayLen(self, target: int, nums):
        s, e = 0, 0
        res = float("inf")
        temp = res
        size = 0
        while e <= len(nums) and s < len(nums):
            if size < target:
                if e == len(nums):
                    break
                size += nums[e]
                e += 1
                if size >= target:
                    res = min(res,e - s)
            else:
                size -= nums[s]
                s += 1
                if size >= target:
                    res = min(res,e - s)
        if res == temp:
            return 0
        return res