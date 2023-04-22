nums = [1,2,3,4,5,6,7,8]
nums.append(1)
print(nums)class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k >= len(nums):
            k -= len(nums)
        e = len(nums) - k
        temp = nums[e:]
        temp2 = nums[:e]
        temp3 = temp + temp2
        for i in range(len(nums)):
            nums[i] = temp3[i]