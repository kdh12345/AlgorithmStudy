import sys
s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

def dfs(t):
    if s == t:
        print(1)
        sys.exit(0)
    if len(t) == 0:
        return 0

    if t[-1] == 'A': #끝이 A이면 끝 제거
        dfs(t[:-1])
    if t[0] == 'B': # 첫 문자 B일 경우 제거 후 뒤집기
        dfs(t[1:][::-1])

dfs(t)
print(0)