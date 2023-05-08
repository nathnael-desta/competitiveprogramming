class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res = [0]
        for trip in trips:
            if len(res) < trip[2] + 2:
                res = res + ([0] * (trip[2] + 2 - len(res)))
            res[trip[1] + 1] += trip[0]

            res[trip[2] + 1] -= trip[0]

        for i in range(1, len(res)):
            res[i] += res[i - 1]
            if res[i] > capacity:
                return False

        return True