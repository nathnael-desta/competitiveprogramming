class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        xor = [0] * len(arr)
        for i in range(len(arr)):
            if i == 0:
                xor[i] = arr[i]
            else:
                xor[i] = arr[i] ^ xor[i - 1]

        for (b, e) in queries:
            if b == 0:
                res.append(xor[e])
            else:
                res.append(xor[e] ^ xor[b - 1])
        return res