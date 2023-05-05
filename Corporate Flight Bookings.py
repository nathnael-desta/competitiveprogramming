class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        lis = [0] * (n + 2)
        for (start, end, num) in bookings:
            lis[start] += num
            lis[end + 1] -= num
        print(lis)
        for i in range(1,len(lis)):
            lis[i] += lis[i - 1]
        return lis[1:-1]