class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        x = len(nums)
        res = [0]*len(nums)
        j = 0
        count = 0
        for i in nums:
            if count == 0 and j < x:
                res[j] = i
                j += 2
            elif count == 0:
                j = 1
                res[j] = i
                count += 1
                j += 2
            else:
                res[j] = i
                j += 2
        print(res)
        return res