class Solution:
    def finalPrices(self, prices):
        stack = []
        results = []
        for i in range(len(prices)-1,-1,-1):
            if len(stack) == 0:
                results.append(prices[i])
            elif (stack[-1] <= prices[i]) and (len(stack) > 0):
                results.append(prices[i] - stack[-1])
            elif (stack[-1] > prices[i]) and (len(stack) > 0):
                while stack and (stack[-1] > prices[i]):
                    stack.pop()
                if not stack:
                    results.append(prices[i])
                else:
                    results.append(prices[i] - stack[-1])
            stack.append(prices[i])
        
        return results[::-1]
