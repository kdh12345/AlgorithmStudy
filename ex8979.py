import sys
n,k = map(int,sys.stdin.readline().split())

result_arr = []
for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    country = arr[0]
    gold = arr[1]
    silver = arr[2]
    bronze = arr[3]

    result_arr.append([country, gold, silver, bronze])

result_arr.sort(key=lambda x:(-x[1], -x[2], -x[3]))

idx = [result_arr[i][0] for i in range(n)].index(k)

ans = 0
for i in range(len(result_arr)):
    if result_arr[idx][1:] == result_arr[i][1:]:
        print(i+1)
        break
