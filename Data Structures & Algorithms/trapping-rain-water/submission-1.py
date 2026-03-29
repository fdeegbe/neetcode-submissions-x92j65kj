class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        l, r, res = 0, len(height)-1, 0
        lmax, rmax = height[0], height[r]
        while l <= r:
            if lmax <= rmax:
                lmax = max(lmax, height[l])
                res += max(0, lmax-height[l])
                l+=1
            else:
                rmax = max(rmax, height[r])
                res += max(0, rmax-height[r])
                r-=1
        return res
