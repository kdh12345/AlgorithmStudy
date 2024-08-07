word = input()
arr = list(word)

tmp = ''
result = ''
for item in arr:
    tmp += item
    if tmp == 'pi':
        result += tmp
        tmp = ''
    if tmp == 'ka':
        result += tmp
        tmp = ''
    if tmp == 'chu':
        result += tmp
        tmp = ''

if result == word:
    print('YES')
else:
    print('NO')