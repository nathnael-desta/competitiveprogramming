class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sort = sorted(nums)
        result = []

        for i in range(len(sort)):
            if sort[i] == target:
                result.append(i)
        return result