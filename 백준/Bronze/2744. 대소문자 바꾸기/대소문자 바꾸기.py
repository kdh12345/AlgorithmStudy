import sys
input = sys.stdin.readline

word = input()

for item in word:
    if item.isupper() == True:
        print(item.lower(),end='')
    else:
        print(item.upper(),end='')