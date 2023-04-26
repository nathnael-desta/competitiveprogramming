class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = 0
        tokens.sort()
        while tokens:
            if power >= tokens[0]:
                power -= tokens[0]
                res += 1
                tokens.pop(0)
            elif tokens[0] <= power + tokens[-1] and len(tokens) != 1 and res > 0:
                power += tokens[-1]
                res -= 1
                tokens.pop(-1)
            else:
                break

        return res