class Solution:
    def reverseParentheses(self, s: str) -> str:
        list1 = list(s)
        count = 0
        back = ''
        str = ""
        answer = ""
        x = True
        while x :
            if list1[count] == ")":
                ind = list1.index(")") - 1
                list1.pop(list1.index(")"))
                while list1[ind] != "(":
                    str += list1[ind]
                    list1.pop(ind)
                    ind -= 1
                list1.pop(ind)
                count = 0
                for i in list(str):
                    list1.insert(ind, i)
                    ind += 1
                str = ''
                continue

            count += 1
            x = False
            for i in list1:
                if i == "(" or i == ")":
                    x = True
        for i in list1:
            answer += i
        return answer