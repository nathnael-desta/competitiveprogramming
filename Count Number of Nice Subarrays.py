class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        pre_count = {0:1}
        pre_sum = 0
        res = 0
        diff = 0
        for i in nums:
            pre_sum += i
            diff = pre_sum - k
            res += pre_count.get(diff,0)
            pre_count[pre_sum] = 1 + pre_count.get(pre_sum, 0)
        return res