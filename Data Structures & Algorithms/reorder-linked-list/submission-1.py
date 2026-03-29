# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use slow-fast pointer to find the midpoint
        mid = end = head
        while end and end.next:
            # advance the fast pointer
            end = end.next.next
            mid = mid.next
        # mid pointer should be at the middle now
        # reverse the 2nd half

        curr = mid
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # now mid should be reversed. lets place in the elements.
        # curr = head

        curr = head # start of list 1
        mid = prev # start of list 2

        while curr:
            temp = curr.next

            curr.next = mid
            curr = curr.next

            mid = temp

