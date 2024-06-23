import sys
input = sys.stdin.readline

card = [list(input().split()) for _ in range(5)]
colors = [item[0] for item in card]
numbers = [int(item[1]) for item in card]

cnt_color = {'R':0,'B':0,'Y':0,'G':0}
cnt_num = [0 for _ in range(11)]

for i in range(5):
    color, num = card[i][0], int(card[i][1])
    cnt_color[color] += 1
    cnt_num[num] += 1

sort_nums = numbers.copy()
sort_nums.sort()
answer = 0
if 5 in cnt_color.values() and sort_nums[0]+1 == sort_nums[1] and sort_nums[1]+1 == sort_nums[2] and sort_nums[2]+1 == sort_nums[3] and sort_nums[3]+1 == sort_nums[4]:
    answer = max(numbers) + 900
elif 4 in cnt_num:
    answer = cnt_num.index(4) + 800
elif 3 in cnt_num and 2 in cnt_num:
    answer = cnt_num.index(3)*10 + cnt_num.index(2) + 700
elif 5 in cnt_color.values():
    answer = max(numbers) + 600
elif sort_nums[0]+1 == sort_nums[1] and sort_nums[1]+1 == sort_nums[2] and sort_nums[2]+1 == sort_nums[3] and sort_nums[3]+1 == sort_nums[4]:
    answer = max(numbers) + 500
elif 3 in cnt_num:
    answer = cnt_num.index(3) + 400
elif 2 in cnt_num:
    first = cnt_num.index(2)
    num2  = numbers.copy()
    for item in num2:
        if item == first:
            numbers.remove(item)
    cnt_num[first] = 0
    if 2 in cnt_num:
        sec = cnt_num.index(2)
        answer = max(first,sec)*10+min(first,sec)+300
    else:
        answer = first + 200
else:
    answer = max(numbers) + 100

print(answer)