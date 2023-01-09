class Solution:
    def maxArea(self, height: List[int]) -> int:
        mono_stack = []
        x0 = 0
        x1 = len(height) - 1
        while x0 < x1:
            comp = [height[x0],height[x1]]
            mono_stack.append(min(comp)*(x1-x0))
            if height[x0] > height[x1]:
                x1 -= 1
            else:
                x0 += 1
        return(max(mono_stack, default=0))