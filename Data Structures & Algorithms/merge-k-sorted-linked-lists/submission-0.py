# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
         return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                heapq.heappush(heap, (curr.val, curr))
                curr = curr.next
        curr = heapq.heappop(heap)[1]
        head = curr
        while heap:
            curr.next = heapq.heappop(heap)[1]
            curr = curr.next    
            
        return head
