class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []

        for i in range(len(s)):
            c = s[i]

            if c == '(':
                left.append(i)
            elif c == '*':
                stars.append(i)
            else:
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        print(left, stars)
        while left:
            if not stars:
                return False
            if left.pop() > stars.pop():
                return False
        return True