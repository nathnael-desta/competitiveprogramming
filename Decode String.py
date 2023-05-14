class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ind = 0
        while ind < len(s):
            if s[ind] != "]":
                stack.append(s[ind])
                ind += 1
            else:
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                num = ""
                while stack[-1].isdigit():
                    num = stack.pop() + num
                    if not stack:
                        break
                stack.append(string * int(num))
                ind += 1

        return "".join(stack)