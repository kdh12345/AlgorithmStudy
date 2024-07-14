from itertools import combinations

expr = list(input())
indices = []
stk = []
ans = set()

for i in range(len(expr)):
    if expr[i] == '(':
        stk.append(i)
    elif expr[i] == ')':
        indices.append((stk.pop(),i))

for i in range(len(indices)):
    for candi in combinations(indices,i+1):
        tmp = expr[:]
        for item in candi: #괄호제거
            tmp[item[0]] = ''
            tmp[item[1]] = ''
        ans.add(''.join(tmp))

for item in sorted(list(ans)):
    print(item)