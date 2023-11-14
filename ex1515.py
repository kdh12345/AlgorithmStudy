import sys
num_arr = input()
i = 0
while True:
    i += 1
    number = str(i)
    while len(number) > 0 and len(num_arr) > 0:
        if number[0] == num_arr[0]:
            num_arr = num_arr[1:]
        number = number[1:]
    if num_arr == '':
        print(i)
        break