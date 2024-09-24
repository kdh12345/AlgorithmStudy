import sys
input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word == '#':
        break
    arr = list(word)
    cnt = 0
    for item in arr:
        if item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u':
            cnt += 1
        if item == 'A' or item == 'E' or item == 'I' or item == 'O' or item == 'U':
            cnt += 1
    print(cnt)