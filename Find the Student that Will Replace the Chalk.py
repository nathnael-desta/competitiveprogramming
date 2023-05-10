class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        new = k // sum(chalk)
        k = k - (new * sum(chalk))
        print(k)
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]