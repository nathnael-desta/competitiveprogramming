class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        e = len(nums) - 2
        while True:
            if e < 0:
                return nums.reverse()
            elif nums[e] < nums[e + 1]:
                swap = e
                break
            else:
                e -= 1
        e = len(nums) - 1
        while True:
            if nums[e] > nums[swap]:
                nums[e],nums[swap] = nums[swap], nums[e]
                break
            else:
                e -= 1
        nums[swap + 1:] = reversed(nums[swap + 1:])
        return nums