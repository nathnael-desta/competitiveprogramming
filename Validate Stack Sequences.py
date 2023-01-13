class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # pushed = [1,2,3,4,5]
        # popped = [4,5,3,2,1]
        po = 0
        pu = 1
        stack = []
        stack.append(pushed[0])
        count = 0
        while po < len(popped):
            print("pu", pu)
            print("po", po)
            print("stack", stack)
            if stack != []:
                if pu == len(pushed) and popped[po] != stack[-1]:
                    return False
                elif popped[po] == stack[-1]:
                    stack.pop(-1)
                    po += 1
                else:
                    while pu < len(pushed):
                        stack.append(pushed[pu])
                        if popped[po] == stack[-1]:
                            stack.pop(-1)
                            po += 1
                            pu += 1
                            break
                        pu += 1
            else:
                if pu < len(pushed):
                    stack.append(pushed[pu])
                    pu += 1
                elif pu == len(pushed) and popped[po] != stack[-1]:
                    return False
                else:
                    while pu < len(pushed):
                        stack.append(pushed[pu])
                        if popped[po] == stack[-1]:
                            stack.pop(-1)
                            po += 1
                            pu += 1
                            break
                        pu += 1

            count += 1
        return True