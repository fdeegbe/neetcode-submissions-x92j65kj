class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def backtrack(openC, closedC):
            if openC == closedC == n:
                # save the current value
                res.append("".join(stack))
                return 
            
            if openC < n:
                stack.append('(')
                backtrack(openC+1, closedC)
                stack.pop() # reset the stack
            if closedC < openC:
                stack.append(')')
                backtrack(openC, closedC+1)
                stack.pop() # reset the stack
            return
        backtrack(0,0)
        return res
