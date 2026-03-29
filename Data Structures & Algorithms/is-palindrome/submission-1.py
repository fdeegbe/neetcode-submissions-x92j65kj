class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalnum(): # there is isalpha, isanum
                res += char.lower()
        return res[::-1] == res

        