class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_arr = 0
        arr = []
        sum = 0
        arr.append(0)
        dic = {}
        dic[0] = 1
        for i in nums:
            sum += i
            if dic.get(sum-k) != None:
                num_arr += dic[sum-k]
            if dic.get(sum) == None:
                dic[sum] = 1
            else:
                dic[sum] += 1
        return num_arr