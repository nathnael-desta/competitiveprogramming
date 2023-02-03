class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        dic = {}
        result = []


        for i in range(len(nums)):
            if sort[i] not in dic:
                dic[sort[i]] = i
        for i in nums:
            result.append(dic[i])

        return result