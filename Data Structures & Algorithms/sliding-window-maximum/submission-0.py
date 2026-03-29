class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # you could use a treap
        # pairs of (value, index)
        # the heap will get the largest number we insert, and if it is not within range, we will remove it.
        # this eliminates the need for removals within our data struct
        nums = [(-v, k) for k , v in enumerate(nums)]
        treap = nums[:k]
        heapq.heapify(treap)
        res = [-treap[0][0]]
        for i in range(k,len(nums)):
            heapq.heappush(treap, nums[i])
            curr = treap[0]
            print(treap)
            while (i-k)+1 > treap[0][1]: # if we are within range
                print("Dropping ", treap[0][1])
                heapq.heappop(treap)
            print("Indserting ", treap[0][0])
            res.append(-treap[0][0])
        # print(res)
        return res


