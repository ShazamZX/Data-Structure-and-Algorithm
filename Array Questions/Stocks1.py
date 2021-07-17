#best time to sell and buy stocks -1 transaction

def profit_calc(arr):
    buy = arr[0]
    profit = 0
    for i in range(len(arr)):
        buy = min(buy,arr[i]) #stores the minimum price till i
        profit = max(profit,(arr[i]-buy)) #stores maximum profit till i
    return profit

#driver code

print(profit_calc([7,1,5,3,6,4]))
