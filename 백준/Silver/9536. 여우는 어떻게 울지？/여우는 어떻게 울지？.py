import sys

t = int(input())

for _ in range(t):
    arr = []
    while True:
        word = str(sys.stdin.readline().rstrip())
        if word == 'what does the fox say?':
            break
        arr.append(word)
    dic = dict()
    for item in arr:
        if 'goes' in item:
            tmp = item.split(' ')
            dic[tmp[2]] = tmp[0]

    result = ''
    for item in arr:
        if 'goes' not in item:
            tmp = item.split(' ')
            for w in tmp:
                if w not in dic:
                    result +=w+' '
    result = result[:-1]
    print(result)