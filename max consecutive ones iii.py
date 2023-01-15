class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = max_len = 0
        for r, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[l]

                l += 1
            else:
                max_len = max(max_len, r - l + 1)
        return max_len