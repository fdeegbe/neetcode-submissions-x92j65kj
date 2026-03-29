class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # determine the cases, calc the max
        res = 0
        stack = []
        # 3 cases, increasing, decreasing, or the same
        for idx, curr in enumerate(heights):
            if not stack or stack[-1][1] < curr: # empty or next number is bigger
                stack.append((idx, curr))
            elif stack[-1][1] > curr: # if the next number is smaller:
                # calc the maxes till u get to lower or empty
                while stack and stack[-1][1] >= curr:
                    pIdx, pVal = stack.pop()
                    print(pIdx,pVal, pVal * (idx - pIdx))
                    res = max(res, pVal * (idx - pIdx))
                stack.append((pIdx, curr))
        while stack:
            pIdx, pVal = stack.pop()
            print(pIdx,pVal, pVal * (len(heights) - pIdx))
            res = max(res, pVal * (len(heights) - pIdx))
        return res