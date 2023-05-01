class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b, e = 0, 0
        dic = {}
        maxim = 0
        if s == "":
            return 0
        while True:
            if dic.get(s[e], 0) == 0:
                dic[s[e]] = 1
                maxim = max(maxim, e - b + 1)
                e += 1
            else:
                dic[s[b]] = 0
                b += 1
            if e >= len(s):
                break

        return maxim