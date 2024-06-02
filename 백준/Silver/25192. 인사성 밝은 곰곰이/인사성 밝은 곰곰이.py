import sys

n =int(sys.stdin.readline().rstrip())
c_set = set()
cnt = 0
for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd != "ENTER":
        if cmd not in c_set:
            cnt+=1
            c_set.add(cmd)
    elif cmd == "ENTER":
        c_set.clear()

print(cnt)