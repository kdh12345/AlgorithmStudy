import sys
text=[]
for _ in range(5):
    arr=list(sys.stdin.readline().strip())
    text.append(arr)
for i in range(max([len(e) for e in text])):
    for j in range(5):
        if i<len(text[j]):
            print(text[j][i],end='')