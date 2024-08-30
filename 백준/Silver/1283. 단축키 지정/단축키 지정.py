n = int(input())

alpha = []
for _ in range(n):
    words = list(input().split())

    flag = False
    for i in range(len(words)):
        if words[i][0].upper() not in alpha:
            alpha.append(words[i][0].upper())
            flag = True
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            print(' '.join(words))
            break

    if flag == False:
        for i in range(len(words)):
            chk = False
            for j in  range(len(words[i])):
                if words[i][j].upper() not in alpha:
                    alpha.append(words[i][j].upper())
                    flag = True
                    chk = True
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j + 1:]
                    print(' '.join(words))
                    break
            if chk == True:
                break
    if flag == False:
        print(' '.join(words))