import sys
input = sys.stdin.readline

n = int(input())
max_lst = []
for i in range(1,n+1):
    my_lst = [n]
    my_lst.append(i)

    idx = 1
    while True:
        nxt_num = my_lst[idx-1] - my_lst[idx]
        if nxt_num < 0:
            break
        my_lst.append(nxt_num)
        idx += 1
    if len(max_lst) < len(my_lst):
        max_lst = my_lst

print(len(max_lst))
for item in max_lst:
    print(item,end= ' ')