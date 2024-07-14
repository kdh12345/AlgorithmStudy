s = input()
k = input()


new_str = ''
for item in s:
    if item.isalpha():
        new_str += item
if k in new_str:
    print(1)
else:
    print(0)