class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            compIdx = i
            if stack:
                compIdx = stack[-1][1] # index of the bigger number in the stack
            res.append(compIdx - i)
            stack.append((temperatures[i], i))
            print(stack)
        print(res)
        res.reverse()
        return(res)

        # what if we push values that are only dec? and their index?
        # (28 6), # (40, 5), (35, 4)
        # (40, 5), (36, 3)
        # (40, 5), (36, 3) (30, 2)
        # (40, 5),
        # algo: push vals on to a stack. if empty, push 0. 
        # pop off untill u find a number bigger than curr or is empty(0) and put the index - i as result
        # push current val and its index on the stack.