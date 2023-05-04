class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        s, e = 0, k - 1
        total = sum(arr[s:e + 1])
        while e < len(arr):
            if total / k >= threshold:
                res += 1
            if e == len(arr) - 1:
                break
            total -= arr[s]
            total += arr[e + 1]
            s += 1
            e += 1

        return res