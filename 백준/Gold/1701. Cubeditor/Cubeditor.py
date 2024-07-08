def make(word):
    table = [0]*len(word)
    j = 0
    for i in range(1,len(word)):
        while j>0 and word[i]!=word[j]:
            j = table[j-1]
        if word[i] == word[j]:
            j += 1
            table[i] = j
    return max(table)

str = input()
ans = 0
for i in range(len(str)):
    ans = max(ans,make(str[i:len(str)]))
print(ans)