class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        s, e = 0, len(people) - 1
        res = 0
        while True:
            if s == e:
                res += 1
                break
            if s > e:
                break
            if people[e] + people[s] <= limit:
                res += 1
                s += 1
                e -= 1
            else:
                res += 1
                e -= 1

        return res