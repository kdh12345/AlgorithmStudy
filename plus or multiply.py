word=input()
ans=int(word[0])
for i in range(1,len(word)):
    if ans==0 or word[i]=='0':
        ans+=int(word[i])
    else:
        ans*=int(word[i])
print(ans)