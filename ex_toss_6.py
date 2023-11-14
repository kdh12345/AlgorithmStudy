import sys
steps_one = [1,2,3]
names_one = ['james', 'bob', 'alice']
steps_two = [10, 20, 30]
names_two = ['james', 'alice', 'bob']
steps_three = [1000, 1, 1]
names_three = ['bob', 'alice', 'james']

res1 = dict()
for i in range(len(steps_one)):
    if names_one[i] in res1:
        if res1[names_one[i]] < steps_one[i]:
            res1[names_one[i]] = steps_one[i]
    elif names_one[i] not in res1:
        res1[names_one[i]] = steps_one[i]

res2 = dict()
for i in range(len(steps_two)):
    if names_two[i] in res2:
        if res2[names_two[i]] < steps_two[i]:
            res2[names_two[i]] = steps_two[i]
    elif names_two[i] not in res2:
        res2[names_two[i]] = steps_two[i]

res3 = dict()
for i in range(len(steps_three)):
    if names_three[i] in res3:
        if res3[names_three[i]] < steps_three[i]:
            res3[names_three[i]] = steps_three[i]
    elif names_three[i] not in res3:
        res3[names_three[i]] = steps_three[i]

result = dict()
for k,v in res1.items():
    if k in result:
        result[k] += v
    elif k not in result:
        result[k] = v

for k,v in res2.items():
    if k in result:
        result[k] += v
    elif k not in result:
        result[k] = v

for k,v in res3.items():
    if k in result:
        result[k] += v
    elif k not in result:
        result[k] = v

print(result)
ans = []
for k,v in result.items():
    ans.append([k,v])
ans.sort(key=lambda x:-x[1])
answer = []
for item in ans:
    answer.append(item[0])
print(answer)