class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        l = list(s)
        dic = collections.Counter(l)
        res = []
        s, e = 0, 0
        letters = {}
        while e < len(l):
            if len(l) == 1:
                res.append(1)
                break
            letter = l[s]
            while letters.get(letter, 0) != dic[letter]:
                letters[l[e]] = letters.get(l[e], 0) + 1
                e += 1

            while s != e:
                letter = l[s]
                if letters.get(letter, 0) == dic[letter]:
                    s += 1
                else:
                    letters[l[e]] = letters.get(l[e], 0) + 1
                    e += 1

            res.append(e)
            l = l[e:]
            s, e = 0, 0
        return (res)