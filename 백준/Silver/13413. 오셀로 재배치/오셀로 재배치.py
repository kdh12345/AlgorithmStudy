import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    cnt_w = 0
    cnt_b = 0
    data1 = input().rstrip()
    data2 = input().rstrip()
    for i in range(n):
        if data1[i] != data2[i]:
            if data1[i] == 'W':
                cnt_w += 1
            else:
                cnt_b += 1
    ans = max(cnt_w,cnt_b)
    print(ans)