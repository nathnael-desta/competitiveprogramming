class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        array = []
        array2 = []
        y = ""
        for i in range(len(arr)):
            array.append(0)
        for i in arr:
            x = int(i[len(i) - 1])
            array[x-1] = i
        for i in array:
            i = i[:-1]
            array2.append(i)
        y = " ".join(array2)
        return y