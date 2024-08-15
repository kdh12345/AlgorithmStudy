import sys
input = sys.stdin.readline

idx = 1
result = []
while True:
    n = int(input())
    if n == 0:
        break
    name_dic = dict()
    for i in range(1,n+1):
        name = str(input())
        name_dic[i] = name
    num_dic = dict()
    for i in range(2*n-1):
        number,alpha = map(str,input().split())
        number = int(number)
        if number in num_dic:
            num_dic[number] += 1
        elif number not in num_dic:
            num_dic[number] = 1

    for k,v in num_dic.items():
        if v < 2:
            result.append(name_dic[k])
    idx += 1

for idx,val in enumerate(result):
    print(idx+1, val,end='')