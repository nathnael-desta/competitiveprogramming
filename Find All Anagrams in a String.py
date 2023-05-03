class Solution:
    def findAnagrams(self, s: str, p: str):
        an = {}
        for i in p:
            an[i] = an.get(i, 0) + 1
        b, e = 0, 0
        dic = {}
        res = []
        while e < len(s):
            if s[e] not in dic and s[e] in an:
                dic[s[e]] = dic.get(s[e], 0) + 1
                e += 1
            elif s[e] not in an:
                e += 1
                b = e
                dic = {}
            elif an[s[e]] <= dic[s[e]]:
                dic[s[b]] = dic.get(s[b], 0) - 1
                if dic[s[b]] == 0:
                    del dic[s[b]]
                b += 1
            else:
                dic[s[e]] = dic.get(s[e], 0) + 1
                e += 1

            if dic == an:
                res.append(b)
                dic[s[b]] = dic.get(s[b], 0) - 1
                if dic[s[b]] == 0:
                    del dic[s[b]]
                b += 1

        return res

rand = Solution()
print(rand.findAnagrams("cbaebabacd","abc"))