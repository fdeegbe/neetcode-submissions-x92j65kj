class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res, a, b = 0,0,0
        for item in tokens:
            if item[-1].isnumeric():
                stack.append(int(item))
            else:
                if item == "+":
                    res = stack.pop() + stack.pop()
                elif item == '-':
                    res = -(stack.pop() - stack.pop())
                elif item == '*':
                    res = stack.pop() * stack.pop()
                elif item == '/':
                    print(item, "WGY*GAFOUIHWSHPDFWEQ")
                    res = (1/stack.pop()) * stack.pop()
                print(res)
                stack.append(int(res))
        return int(stack[0])
        
