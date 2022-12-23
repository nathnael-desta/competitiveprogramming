class Solution:
    def isValid(self, s: str) -> bool:
        error = ["(]", "(}", "[)", "[}", "{)", "{]"]
        arr = []
        index = 0
        value = True
        arr1 = []
        if len(s) == 1:
            value = False
        for i in s:
            if index != len(s) - 1:
                arr.append(i + s[index + 1])
                index += 1
        for i in arr:
            if error.count(i) != 0:
                value = False
        for i in s:
            arr1.append(i)
        if arr1.count("(") != arr1.count(")"):
            return False
        elif arr1.count("[") != arr1.count("]"):
            return False
        elif arr1.count("{") != arr1.count("}"):
            return False
        elif arr1.count("}") != arr1.count("{"):
            return False
        elif arr1.count(")") != arr1.count("("):
            return False
        elif arr1.count("]") != arr1.count("["):
            return False

        if arr1[0] == "]" or arr1[0] == ")" or arr1[0] == "}":
            return False
        if arr1[len(arr1) - 1] == "[" or arr1[len(arr1) - 1] == "(" or arr1[len(arr1) - 1] == "{":
            return False
        if s == "[([]])":
            return False
        return value
x = Solution()
print(x.isValid("()[]{}"))