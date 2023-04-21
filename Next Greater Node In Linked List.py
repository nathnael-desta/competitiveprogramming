# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        cur = head
        ind = 0
        lis = []
        while cur != None:
            lis.append([cur.val, ind])
            ind += 1
            cur = cur.next

        stack = [lis[0]]
        res = [0] * len(lis)

        for i in lis[1:]:
            while len(stack) > 0:
                if i[0] > stack[-1][0]:
                    res[stack[-1][1]] = i[0]
                    stack.pop()
                else:
                    break
            stack.append(i)
        print(lis)
        return res