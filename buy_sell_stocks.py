prices=[5,3,4,5,6]
profit=0
buy=0

for sell in range(1,len(prices)):
    current_profit= prices[sell]-prices[buy]
    profit=max(profit,current_profit)
    if prices[sell]<prices[buy]:
        buy=sell
print(profit)