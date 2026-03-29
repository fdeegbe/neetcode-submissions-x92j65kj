# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dummy = ListNode(val=None, next=head)

        for _ in range(n-1):
            head = head.next

        curr = dummy

        while head.next != None:
            # print(head.val, curr.val)
            curr = curr.next
            head = head.next
        temp = curr
        # print(temp.val)
        curr = curr.next
        temp.next = curr.next
        return dummy.next