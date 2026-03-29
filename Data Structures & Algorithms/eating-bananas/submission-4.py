class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # how do we determine the ranges of k to check? 
        # the upper bound would be max(piles)
        # the minimun should be...
        # h has to be greater than or equal to the number of piles
        def blackbox(lst,kval): # retuirns how many hours we need at  rate k
            return sum([math.ceil(num/kval) for num in lst])
        # binary search this blackbox for the correct soln
        l,r = 1, max(piles)
        m = l + (r-l) // 2

        while l <= r:
            if blackbox(piles, m) > h: # you need a higher m val because you can eat the banannas faster
                l = m + 1
            elif blackbox(piles, m) <= h: # you need a lower m value OR youre at that m value.. it will always be behind
                r = m - 1
            m = l + (r-l) // 2

        print(l)
        return l