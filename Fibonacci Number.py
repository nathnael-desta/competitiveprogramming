class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        def fibo(n):
            if n < 2:
                return n
            else:
                return fibo(n - 1) + fibo(n - 2)
        return fibo(n - 1) + fibo(n - 2)