class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        s, e = 0, 1
        if len(arr) < 3:
            return 0
        res = 0
        while e < len(arr):
            count = 0
            while e < len(arr):
                if arr[s] < arr[e]:
                    count += 1
                    s += 1
                    e += 1
                else:
                    break
                print(s, e, count)
            if count >= 1:
                if e >= len(arr):
                    break
                if arr[s] <= arr[e]:
                    s += 1
                    e += 1
                    continue
                while e < len(arr):
                    if arr[s] > arr[e]:
                        count += 1
                        s += 1
                        e += 1
                    else:
                        break
                count += 1
            else:
                count = 0
                s += 1
                e += 1
            res = max(res, count)
        return res