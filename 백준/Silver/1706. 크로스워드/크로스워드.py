import sys
input = sys.stdin.readline

r,c = map(int,input().split())
board = []
for _ in range(r):
    arr = list(input().rstrip())
    board.append(arr)

result = []
for i in range(r):
    word = ''
    for j in range(c):
        if board[i][j] != '#':
            word += board[i][j]
        elif len(word) >= 2:
            result.append(word)
        else:
            word = ''
    if len(word) >= 2:
        result.append(word)

for i in range(c):
    word = ''
    for j in range(r):
        if board[j][i] != '#':
            word += board[j][i]
        elif len(word) >= 2:
            result.append(word)
        else:
            word = ''

    if len(word) >= 2:
        result.append(word)

result.sort()
ans = result[0]
print(ans)