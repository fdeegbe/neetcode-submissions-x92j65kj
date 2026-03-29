class Solution:
    def checkValidString(self, s: str) -> bool:
        pmax = pmin = 0
        #pMin: the minimum possible number of open left parentheses ( that could still be unmatched at this point in the string.
        #pMax: the maximum possible number of open left parentheses ( that could still be unmatched at this point in the string.
        for i in range(len(s)):
            c = s[i]
            if c == '(': # one more open across the board
                pmax += 1
                pmin += 1
            elif c == '*': # could be opening a new paren, or closing an old one
                pmax += 1
                pmin -= 1
            else: # def closing a paren
                pmax -= 1
                pmin -= 1
            pmin = max(pmin, 0) # clamp the possible range to zero to ensure proper bounds
            if pmax < 0:
                return False
            # too many ')' to the point where the best case is unrecoverable
        return pmin == 0
        # if pmin returns 0, then we know that in the most pessimistic case (always ')' and ' ' if not) there is at least one solution there