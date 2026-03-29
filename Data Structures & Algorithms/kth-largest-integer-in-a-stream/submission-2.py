class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      nums = [-n for n in nums]
      heapq.heapify(nums)
      self.mh = nums
      self.k=k

    def add(self, val: int) -> int:
      heapq.heappush(self.mh, -val)
      c = self.mh.copy()
      for _ in range(self.k):
         val = heapq.heappop(c)
         print(val)

      return -val