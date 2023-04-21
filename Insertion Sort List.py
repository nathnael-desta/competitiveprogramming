# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        cur = head
        while cur != None:
            res.append(cur.val)
            cur = cur.next

        for i in range(1, len(res)):
            j = i
            while res[j - 1] > res[j] and j > 0:
                res[j - 1], res[j] = res[j], res[j - 1]
                j -= 1

        linked = ListNode(res[0])
        cur = linked
        for i in range(1, len(res)):
            new_node = ListNode(res[i])
            cur.next = new_node
            cur = cur.next
        return linked