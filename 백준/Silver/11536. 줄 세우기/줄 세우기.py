n = int(input())

arr = []
for _ in range(n):
    name = input()
    arr.append(name)

in_name = sorted(arr)
de_name = sorted(arr,reverse=True)

if in_name == arr:
    print('INCREASING')
elif de_name == arr:
    print('DECREASING')
else:
    print('NEITHER')