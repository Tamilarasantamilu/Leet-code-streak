class Solution:
    def diffWaysToCompute(self, expression: str, memo = {}) -> List[int]:
        if expression in memo:
            return memo[expression]

        result = []
        operators = "*-+"
        if expression.isdigit():
            return [int(expression)]
        for i,c in enumerate(expression):
            if c in operators:
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i + 1:])
                for r1 in res1:
                    for r2 in res2:
                        result.append(eval(str(r1) + c + str(r2)))
        
        memo[expression] = result
        return result
