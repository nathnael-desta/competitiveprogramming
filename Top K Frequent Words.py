class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        freq = [[] for i in range(len(words) + 1)]

        for i in words:
            dic[i] = 1 + dic.get(i, 0)

        for w, i in dic.items():
            freq[i].append(w)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            freq[i] = sorted(freq[i])
            for w in freq[i]:
                res.append(w)
                if len(res) == k:
                    return res
        return res
