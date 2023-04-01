class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = {}
        freq = [[] for i in range(len(arr) + 1)]

        for n in arr:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        print(freq)

        newarr = []
        count = 0
        items = 0
        length = len(arr) / 2
        for i in range(len(freq) - 1, 0, -1):
            if count < length:
                if freq[i] != []:
                    for j in freq[i]:
                        if count < length:
                            count += i
                            items += 1
                        else:
                            return items
            else:
                return items
        return items

        return count