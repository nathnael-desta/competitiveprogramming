# User function Template for python3

class Solution:
    def select(self, arr, i):
        # code here
        return i

    def selectionSort(self, arr, n):
        # code here
        array1 = arr
        newArr = []
        num = 0
        for i in range(len(arr)):
            x = min(array1)
            y = array1.index(x)
            z = array1.pop(y)
            newArr.insert(num, z)
            num += 1

            # if z == select(arr,4):
            #   newArr += arr
            #  break
        # print(newArr)
        while len(arr) != n:
            arr.append(0)
        for i in range(len(arr)):
            arr[i] = newArr[i]

            # if z == select(arr,4):
            #    newArr += arr
            #    break


# { for Pytho
# Driver Code Starts
# Initial Template n 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends