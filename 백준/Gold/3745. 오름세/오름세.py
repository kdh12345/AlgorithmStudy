import sys
from bisect import bisect_left
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        prices = list(map(int,input().split()))

        dp = [1]

        arr = [prices[0]]

        for i in range(1,n):
            idx = bisect_left(arr,prices[i])

            if idx == len(dp):
                dp.append(dp[-1]+1)

                arr.append(prices[i])
            else:
                arr[idx] = prices[i]
        print(dp[-1])
    except:
        break