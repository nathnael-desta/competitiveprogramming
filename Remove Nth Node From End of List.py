# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_node = head
        if head != None:
            len = 1
            while curr_node.next != None:
                len += 1
                curr_node = curr_node.next
        else:
            len = 0
        ind = len - n
        x = 1
        curr_node = head
        if ind == 0:
            head = head.next
            return head
        while curr_node.next != None:
            last_node = curr_node
            curr_node = curr_node.next
            if ind == x:
                last_node.next = curr_node.next
                return head
            x += 1
        print(len, x, ind)