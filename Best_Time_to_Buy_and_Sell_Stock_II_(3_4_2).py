prices = [7,1,5,3,6,4]
profit=0
for i in range(len(prices)-1):
    if prices[i+1]<=prices[i]:
        continue
    else:
        profit +=prices[i+1]-prices[i]
print(profit)