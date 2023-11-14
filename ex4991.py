import sys
from collections import deque
from itertools import permutations

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def bfs(board, r, c, sx, sy):
    dq = deque([(sx, sy)])
    visit = [[0] * c for _ in range(r)]
    visit[sx][sy] = 1
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0:
                if board[nx][ny] != 'x':
                    dq.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1

    return visit


while True:
    c, r = map(int, sys.stdin.readline().split())
    if c == 0 and r == 0:
        break
    board = []
    for _ in range(r):
        arr = list(sys.stdin.readline().rstrip())
        board.append(arr)
    sx = 0
    sy = 0
    dusts = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'o':
                sx = i
                sy = j
            elif board[i][j] == '*':
                dusts.append((i, j))

    visited = bfs(board, r, c, sx, sy)
    cleaner = [0] * len(dusts)
    is_clean = True
    for idx, rc in enumerate(dusts):
        tmp = visited[rc[0]][rc[1]]
        if not tmp:
            print(-1)
            is_clean = False
            break
        cleaner[idx] += tmp - 1

    if is_clean == True:
        dists = [[0] * (len(dusts)) for _ in range(len(dusts))]
        for i in range(len(dusts) - 1):
            visited = bfs(board, r, c, dusts[i][0], dusts[i][1])
            for j in range(i + 1, len(dusts)):
                dists[i][j] = visited[dusts[j][0]][dusts[j][1]] - 1
                dists[j][i] = dists[i][j]
        ans = int(1e9)
        for li in permutations(range(len(dists))):
            tmp = cleaner[li[0]]
            start = li[0]
            for idx in range(1, len(li)):
                end = li[idx]
                tmp += dists[start][end]
                start = end
            ans = min(ans, tmp)
        print(ans)
