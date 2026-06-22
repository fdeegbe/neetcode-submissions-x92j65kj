class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = float('-inf')
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = currMax
            currMax = max(currMax, temp)
        arr[-1] = -1
        return arr