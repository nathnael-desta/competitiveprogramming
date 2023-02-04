class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if 0 < n < 3:
            if n == 1:
                return True
            else:
                return False
        else:
            while n >= 3:
                n = n / 3
            if n == 1:
                return True
            else:
                return False
