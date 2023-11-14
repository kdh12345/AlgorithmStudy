levels = [1,2,3,4]
levels.sort()
nanido = len(levels) // 4
res = levels[-nanido:]
ans = max(res)
print(ans)