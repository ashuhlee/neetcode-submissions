import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for item in tokens:
            # operator check
            if item in ops:
                right = stack.pop()
                left = stack.pop()

                res = int(ops[item](left, right))
                stack.append(res)
            # digit check
            else:
                stack.append(int(item))
        
        return stack.pop()