import sys

n,m = map(int,sys.stdin.readline().split())

key_dic = dict()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    key_dic[word] = 1

ans = n
for _ in range(m):
    input_arr = sorted(sys.stdin.readline().rstrip().split(','))

    for item in input_arr:
        if item in key_dic.keys():
            if key_dic[item] == 1:
                key_dic[item] -= 1
                ans -= 1
    print(ans)