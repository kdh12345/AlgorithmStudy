import sys
n = int(sys.stdin.readline().rstrip())
sangduk = 100
changyoung = 100
for _ in range(n):
    num1,num2=map(int,sys.stdin.readline().split())
    if num1 < num2:
        changyoung -= num2
    elif num1 > num2:
        sangduk -= num1

print(changyoung)
print(sangduk)