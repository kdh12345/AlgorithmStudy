import sys
money= 10
stocks = [ [1,1], [3,5], [3,5], [4,9] ]

if len(stocks) == 1:
    if stocks[0][1] > money:
        print(0)
        exit(0)
    else:
        print(stocks[0][0])
        exit(0)
stocks.sort()
s = 0
e = len(stocks) - 1
max_val = 0
while s<e:
    total_price = stocks[s][1] + stocks[e][1]
    total_val = 0
    if total_price <= money:
        total_val = stocks[s][0] + stocks[e][0]
        if max_val < total_val:
            max_val = total_val
    s+=1
    e-=1
print(max_val)
