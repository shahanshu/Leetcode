def fp(prices):
    stack=[]
    for i in range(len(prices)):
        while stack and prices[i] <=prices[stack[-1]]:
            prices[stack.pop()]-=prices[-1]
        stack.append(prices[i])
    return prices


