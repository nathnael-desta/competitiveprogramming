class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-int(x) for x in nums]
        print(nums)
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
            print(res)
        return str(-res)