#best time to buy and sell stocks two transactions allowed

def maxprofit(prices):
    profit = 0
    for i in range(1,len(prices)):
        diff = prices[i] - prices[i-1]
        if diff>0:
            profit+=diff
    return profit


#driver code

prices = [7,1,5,3,6,4]

print(maxprofit(prices))