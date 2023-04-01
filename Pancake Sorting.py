class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        count = 0
        while len(arr) != 0:
            maxim = arr.index(max(arr))
            temp = arr[:maxim + 1]
            temp.reverse()
            arr[:maxim + 1] = temp
            res.append(maxim + 1)
            arr.reverse()
            count += 1
            if count % 2 == 0:
                arr.pop(-1)
        return res