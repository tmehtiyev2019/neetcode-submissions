class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ["+", "*","-",'/']:
                stack.append(t)
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(int(a)+int(b))
                if t == "*":
                    stack.append(int(a)*int(b))
                if t == "-":
                    stack.append(int(a)-int(b))
                if t == "/":
                    stack.append((int(a)/int(b)))
        return int(stack[0])

                

