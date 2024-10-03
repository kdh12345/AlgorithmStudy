import sys
input = sys.stdin.readline
def cursor_down(cur):
    cur += 1
    print(1,end='')
    return cur
def c_up(cur):
    if cur > 0:
        c_lst[cur], c_lst[cur-1] = c_lst[cur-1],c_lst[cur]
        cur -= 1
        print(4,end='')
    return cur

c_lst = []
n = int(input())
for _ in range(n):
    c_lst.append(input().rstrip())

cur = 0
while True:
    if c_lst[cur] != 'KBS1':
        cur = cursor_down(cur)
    else:
        cur = c_up(cur)
    if c_lst[0] == 'KBS1':
        break

while True:
    if c_lst[cur] != 'KBS2':
        cur = cursor_down(cur)
    else:
        cur = c_up(cur)
    if c_lst[1] == 'KBS2':
        break