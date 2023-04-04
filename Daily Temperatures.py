class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            if stack == []:
                stack.append([i, v])
            elif stack[-1][1] < v:
                while stack != []:
                    if stack[-1][1] < v:
                        res[stack[-1][0]] = i - stack[-1][0]
                        stack.pop()
                    else:
                        break
                stack.append([i, v])

            else:
                stack.append([i, v])
        return res