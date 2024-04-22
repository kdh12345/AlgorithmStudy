import sys
input = sys.stdin.readline

n = int(input())

ans = 0
st = []
for _ in range(n):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        if cmd[2] == 1:
            ans += cmd[1]
        else:
            st.append([cmd[1],cmd[2]-1])
        continue

    if len(st) > 0:
        st[-1][1] -= 1
        if st[-1][1] == 0:
            x = st[-1]
            st.pop()
            ans += x[0]

print(ans)