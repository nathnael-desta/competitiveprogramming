class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        res = 0
        for i in nums:
            if dic.get(k - i):
                if dic[k - i] > 0:
                    res += 1
                    dic[k - i] -= 1
                else: 
                    if dic.get(i):
                        dic[i] += 1
                    else:
                        dic[i] = 1
            else:
                if dic.get(i):
                        dic[i] += 1
                else:
                    dic[i] = 1
        return res