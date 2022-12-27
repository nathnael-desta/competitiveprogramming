class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #nums = [-1,-1,-1,-1,-1,-1]
        rev_nums = nums.copy()
        rev_nums.reverse()
        nums.insert(0,0)
        rev_nums.insert(0,0)
        pre_sum_fw = [0] * len(nums) #[1, 8, 11, 17, 22, 28]
        pre_sum_rv = [0] * len(rev_nums) #[6, 11, 17, 20, 27, 28]
        count = 0
        for i in range(0, len(nums)):
            pre_sum_fw[i] = pre_sum_fw[i - 1] + nums[i]
        for i in range(0, len(rev_nums)):
            pre_sum_rv[i] = pre_sum_rv[i - 1] + rev_nums[i]


        pre_sum_rv.reverse()
        pre_sum_rv.pop(0)
        pre_sum_fw.pop(len(pre_sum_fw)-1)


        print(pre_sum_fw)
        print(pre_sum_rv)
        for i in range(len(pre_sum_fw)):
            if pre_sum_rv[i] == pre_sum_fw[i]:
                return i
        return -1