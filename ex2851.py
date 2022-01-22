import sys
numbers=[]
for _ in range(10):
    num=int(sys.stdin.readline().rstrip())
    numbers.append(num)
numbers.sort()
total=0
prev=0
for num in numbers:
    total+=num
    if total>=100:
        break
    prev=total
ans=max(total,prev)
print(ans)