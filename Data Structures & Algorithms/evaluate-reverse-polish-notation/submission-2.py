# Reverse polish notation --> digit digit operator

# when I take in a number, is it a number or a operator
#     --> if number then, continue on
#     operator: need to operate with numbers I have
#  1 3 + --> 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                operator = token
                if operator == "+":
                    ans = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(ans))
                    print(stack)
                elif operator == "-":
                    ans = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(ans))
                    print(stack)
                elif operator == "*":
                    ans = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(ans))
                    print(stack)
                else:
                    ans = stack[-2] /stack[-1]
                    if ans < 0:
                        ans = math.ceil(stack[-2] / stack[-1])
                    else:
                        ans = stack[-2] // stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(ans))
                    print(stack)
            else:
                stack.append(int(token))
        print(stack)
        return stack.pop()


                
        