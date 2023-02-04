class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            for j in range(nums2.index(i), len(nums2)):
                print(j)
                print(i)
                if nums2[j] > i:
                    result.append(nums2[j])
                    break
                if j == len(nums2) -1:
                    result.append(-1)
        return result