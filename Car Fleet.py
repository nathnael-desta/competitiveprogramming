class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        arr = []
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        arr.sort(reverse=True)

        for i in range(len(position)):
            time.append((target - arr[i][0]) / arr[i][1])
        stack = []
        count = 0
        x = 0
        for i in time:
            if stack == []:
                stack.append(i)
            elif stack[0] < i:
                count += 1
                stack = []
                stack.append(i)
            else:
                stack.append(i)
        if stack != []:
            count += 1
        return count