class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        dic1 = {}
        dic2 = {}
        s1, e1 = 0, firstLen
        s2, e2 = 0, secondLen
        while e1 < len(nums) + 1 or e2 < len(nums) + 1:
            if e1 < len(nums) + 1:
                dic1[(s1, e1)] = sum(nums[s1:e1])
                s1 += 1
                e1 += 1
            if e2 < len(nums) + 1:
                dic2[(s2, e2)] = sum(nums[s2:e2])
                s2 += 1
                e2 += 1
        print(nums)
        print("dic1", dic1)
        print("dic2", dic2)
        maxim = 0
        for k1, v1 in dic1.items():
            for k2, v2 in dic2.items():
                temp = maxim
                if not k1[0] < k2[0] < k1[1] and not k1[0] < k2[1] < k1[1] and not k2[0] < k1[1] < k2[1] and not k2[0] < \
                                                                                                                 k1[0] < \
                                                                                                                 k2[1]:
                    maxim = max(v1 + v2, maxim)
                if not maxim == temp:
                    print(k1, v1, k2, v2, v1 + v2)

        return maxim
rand = Solution()

print(rand.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2)) # check if inclusive