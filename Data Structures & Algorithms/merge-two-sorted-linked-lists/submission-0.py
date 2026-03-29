# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head
        while list1 or list2:
            a = list1.val if list1 else 101
            b = list2.val if list2 else 101
            if a >= b:
                list2 = list2.next
                curr.next = ListNode(b)
            else:
                list1 = list1.next
                curr.next = ListNode(a)
            curr = curr.next
        return head.next