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
        # print(mid.val)


        curr = mid
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # now mid should be reversed. lets place in the elements.
        # curr = head

        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print("JIIOI\n")
        # while prev:
        #     print(prev.val)
        #     prev = prev.next    
        start = head # start of list 1
        mid = prev # start of list 2
        curr = start

        while curr:
            temp = curr.next
            curr.next = mid

            curr = curr.next

            mid = temp
            

            


        # while curr and mid:
        #     temp = curr.next # save the next start val
        #     curr.next = mid # merge

        #     temp2 = mid.next # save next mid val
        #     mid.next = temp  # merge 

        #     mid = temp2
        #     curr = temp
        # curr = head
        # while curr:
        #     curr.next = mid

