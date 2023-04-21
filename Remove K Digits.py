class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = ["0"]
        for i in num:
            if k > 0:
                while int(stack[-1]) > int(i) and k != 0:
                    stack.pop(-1)
                    k -= 1
            stack.append(i)
        while k != 0:
            if len(stack) == 0:
                return "0"
            stack.pop(-1)
            k -= 1
        return str(int("".join(stack)))