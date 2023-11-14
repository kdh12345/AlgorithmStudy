import sys

n,x = map(int,sys.stdin.readline().split())
days = list(map(int,sys.stdin.readline().split()))

if max(days) == 0:
    print("SAD")
else:

    val = sum(days[:x])

    max_val = val
    max_cnt = 1

    for i in range(x,n):
        val += days[i] # 슬라이딩 윈도우 앞

        val -= days[i-x] # 슬라이딩 윈도우 뒤

        if max_val < val:
            max_val = val
            max_cnt = 1
        elif max_val == val: #최대값 여러개
            max_cnt += 1
    print(max_val)
    print(max_cnt)