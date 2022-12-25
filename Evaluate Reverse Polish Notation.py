class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        val = 0
        for i in tokens:
            if i == "+":
                x = num[-2] + num[-1]
                num.pop(-1)
                num.pop(-1)
                num.append(x)
            elif i == "-":
                x = num[-2] - num[-1]
                num.pop(-1)
                num.pop(-1)
                num.append(x)
            elif i == "*":
                x = num[-2] * num[-1]
                num.pop(-1)
                num.pop(-1)
                num.append(x)
            elif i == "/":
                x = num[-2] / num[-1]
                x = int(x)
                num.pop(-1)
                num.pop(-1)
                num.append(x)
            else:
                num.append(int(i))
        return num[0]