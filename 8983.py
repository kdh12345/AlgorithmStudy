import sys
m,n,l = map(int,sys.stdin.readline().split())
man = list(map(int,sys.stdin.readline().split()))
ani = []
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    ani.append((a,b))
man.sort()

cnt = 0
for a,b in ani:
    left = 0
    right = len(man) - 1
    while left < right:
        mid = (left+right) // 2
        if man[mid] < a:
            left = mid + 1
        elif man[mid] > a:
            right = mid - 1
        else:
            left = mid
            break
    if abs(man[left]-a)+b <= l:
        cnt+=1
    elif left + 1 < len(man) and abs(man[left+1]-a)+b <= l:
        cnt+=1
    elif left > 0 and abs(man[left-1]-a)+b <= l:
        cnt+=1
print(cnt)