from collections import deque

'''
Infix to Postfix
https://www.youtube.com/watch?v=vq-nUF0G4fI
'''

def calculate_postfix(postfix):
    stack = deque()
    for token in postfix:
        if token.isdigit():
            stack.append(token)
        elif token in "+-*/":
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if token == "+":
                stack.append(num1+num2)
            elif token == "-":
                stack.append(num1-num2)
            elif token == "*":
                stack.append(num1*num2)
            elif token == "/":
                stack.append(num1//num2)
    return stack[-1]
def infix_to_postfix(tokens):
    def has_higher(op1, op2):
        table = {'*': 2, '/': 2, '+': 1, '-': 1}
        return table[op1] >= table[op2]
    stack = deque()
    result = []
    for token in tokens:
        token: str
        if token.isdigit():
            result.append(token)
        elif token in '+-*/':
            while stack and has_higher(stack[-1], token):
                result.append(stack.pop())
            stack.append(token)
        else:
            raise Exception("Opps")
    while stack:
        result.append(stack.pop())
    return result
def tokenize(s):
    num_str = ''
    result = []
    for ch in s:
        if ch in '0123456789':
            num_str += ch
        elif ch in '+-*/':
            result.append(num_str)
            result.append(ch)
            num_str = ''
    result.append(num_str)
    return result
class Solution:
    def calculate(self, s: str) -> int:
        "s = 33+2*2"
        tokens = tokenize(s) # ['33', '+', '2', '*', '2']
        postfix = infix_to_postfix(tokens) # ['33', '2', '2', *, +]
        result = calculate_postfix(postfix) # 37
        return result

s = "3+2*2"
result = Solution().calculate(s)
assert result == 7

s = "2*2+3"
result = Solution().calculate(s)
assert result == 7

s = " 3/2 "
result = Solution().calculate(s)
assert result == 1

s = " 3+5 / 2 "
result = Solution().calculate(s)
assert result == 5