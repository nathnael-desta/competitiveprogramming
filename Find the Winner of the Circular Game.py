class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [x for x in range(1,n + 1)]
        count = 0
        while len(l) > 1:
            if count + k - 1 <= len(l) - 1: 
                count += k - 1
                l.pop(count)
            else:
                while count + k - 1 > len(l) - 1:
                    count -= len(l)
                count += k - 1
                l.pop(count)
        return l[0]