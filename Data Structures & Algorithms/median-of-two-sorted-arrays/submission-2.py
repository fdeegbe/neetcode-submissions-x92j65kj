class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        N = len(A) + len(B)
        ODD = N % 2 == 1
        print(ODD)

        if len(A) > len(B):
            A, B = B, A # A is always the smaller one
        
        # binary search A for the correct 'split'

        l, r = 0, len(A) - 1

        while True:
            m = l + (r - l) // 2
            Aleft = A[m] if m >= 0 else float('-inf')
            Aright = A[m+1] if m+1 < len(A) else float('inf')

            split = (N//2) - (m+1) - 1
            print(split)
            Bleft = B[split] if split >= 0 else float('-inf')
            Bright = B[split+1] if split+1 < len(B) else float('inf')
            print(Aleft, Aright)
            print(Bleft, Bright)
        
            if Aleft <= Bright and Bleft <= Aright:
                if ODD: 
                    return min(Aright, Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r =  m - 1
            else:
                l = m + 1
        return B[len(B) // 2]

