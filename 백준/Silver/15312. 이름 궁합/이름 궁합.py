hint = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input()
b = input()
arr = []

for i in range(len(a)):
    arr.append(hint[ord(a[i]) - 65])
    arr.append(hint[ord(b[i]) - 65])

tmp = []

while len(arr) != 2:
    for idx in range(1,len(arr)):
        tmp.append((arr[idx]+arr[idx-1]) % 10)

    arr = tmp
    tmp = []

print(f"{arr[0]}{arr[-1]}")