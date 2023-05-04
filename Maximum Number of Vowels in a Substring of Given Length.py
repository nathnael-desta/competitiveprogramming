class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        res = 0
        for i in s[:k]:
            if i in vowels:
                res += 1
        b, e = 0, k
        temp = res
        while e < len(s):
            if s[b] in  vowels:
                temp -= 1
            if s[e] in vowels:
                temp += 1
            res = max(temp, res)
            b += 1
            e += 1
        return res