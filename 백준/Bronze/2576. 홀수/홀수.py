result = []
for _ in range(7):
    number = int(input())
    if number % 2 == 1:
        result.append(number)

if len(result)== 0:
    print(-1)
else:
    ans1 = sum(result)
    ans2 = min(result)
    print(ans1)
    print(ans2)