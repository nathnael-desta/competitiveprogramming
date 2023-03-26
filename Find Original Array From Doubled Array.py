class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dic = collections.Counter(changed)

        if len(changed) == 0 or len(changed) % 2 != 0: return []

        res = []

        if dic.get(0):
            if dic[0] % 2 == 0:
                res.extend([0] * int(dic[0] / 2))
                dic[0] = 0
            else:
                print(0)
                return []

        for i in sorted(dic):
            if dic[i] > 0:
                if int(i / 2) in dic and dic[i / 2] > 0:
                    minlen = min(dic[i], dic[int(i / 2)])
                    res.extend(minlen * [int(i / 2)])
                    dic[i] -= minlen
                    dic[i / 2] -= minlen
                elif int(i * 2) in dic and dic[i * 2] > 0:
                    minlen = min(dic[i], dic[int(i * 2)])
                    res.extend(minlen * [i])
                    dic[i] -= minlen
                    dic[i * 2] -= minlen
                else:
                    print(1)
                    return []
        if sum(dic.values()) != 0:
            return []
        return res