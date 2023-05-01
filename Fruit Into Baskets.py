class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxim = 0
        s, e = 0, 0
        dic = {}
        while e < len(fruits):
            if len(dic.keys()) < 2 or fruits[e] in dic.keys():
                maxim = max(maxim, e - s + 1)
                dic[fruits[e]] = dic.get(fruits[e], 0) + 1
                e += 1
            else:
                dic[fruits[s]] = dic[fruits[s]] - 1
                if dic[fruits[s]] == 0:
                    del dic[fruits[s]]
                s += 1

        return maxim