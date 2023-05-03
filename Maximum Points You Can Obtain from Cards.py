class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s, e = 0, k - 1
        maxim = sum(cardPoints[s:e + 1])
        check = maxim
        count = 0
        while count < k:
            check -= cardPoints[e]
            check += cardPoints[s - 1]
            s = s - 1
            e -= 1
            maxim = max(maxim, check)
            count += 1

        return maxim