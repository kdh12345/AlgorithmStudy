n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
board = [[5] * n for _ in range(n)]
tree = [[dict() for _ in range(n)] for _ in range(n)]

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1][age] = 1

for year in range(k):
    # 봄, 여름
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                temp = dict()
                die = 0
                for age in sorted(tree[i][j].keys()):
                    if age * tree[i][j][age] <= board[i][j]:
                        temp[age + 1] = tree[i][j][age]
                        board[i][j] -= age * tree[i][j][age]
                    else: # summer
                        survive = board[i][j] // age
                        if not survive:  # 생존한 나무가 없음
                            die += (age // 2) * tree[i][j][age]
                            continue
                        board[i][j] -= age * survive
                        temp[age + 1] = survive
                        die += (age // 2) * (tree[i][j][age] - survive)
                tree[i][j] = temp
                board[i][j] += die
    # 가을
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                num = 0
                for age in tree[i][j].keys():
                    if age % 5 == 0:
                        num += tree[i][j][age]
                if num:
                    for d in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if 1 not in tree[nx][ny].keys():
                                tree[nx][ny] = num
                            else:
                                tree[nx][ny] += num
    # 겨울
    for i in range(n):
        for j in range(n):
            board[i][j] += A[i][j]
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += sum(tree[i][j].values())
print(cnt)