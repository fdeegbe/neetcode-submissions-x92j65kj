class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            if carry:
                digits[i] += 1
                carry = 0
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
        if carry:
            digits = [1] + digits
        return digits

