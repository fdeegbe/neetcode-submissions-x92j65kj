class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # print(numbers[4])
        # print(numbers[0])
        i, j = 0, len(numbers)-1
        while i < j:
            print(j)
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]
