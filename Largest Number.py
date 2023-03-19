class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def larger(num1,num2):
            if num1 + num2 > num2 + num1:
                return 0
            else:
                return 1
        for i in range(len(nums)):
            already_sorted = True
            for j in range(len(nums) - i - 1):
                if larger(str(nums[j]), str(nums[j + 1])):
                    nums[j] , nums[j + 1] = nums[j + 1] , nums[j]
                    already_sorted = False
            if already_sorted:
                break
        return str(int("".join(map(str,nums))))