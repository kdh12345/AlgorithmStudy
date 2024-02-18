import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    arr = list(sys.stdin.readline().strip())
    graph.append(arr)

# row
row_cnt = 0
for i in range(n):
    cnt1 = 0
    for j in range(n):
        if graph[i][j] == '.':
            cnt1 += 1
        else:
            cnt1 = 0
        if cnt1 == 2:
            row_cnt +=1


# col
col_cnt = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            col_cnt += 1
            
print(row_cnt,end=' ')
print(col_cnt)