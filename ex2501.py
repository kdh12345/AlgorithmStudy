import sys
n,k = map(int,sys.stdin.readline().split())
aliquot = [] #약수 담는 배열
for i in range(1,n+1):
    if n % i == 0:
        aliquot.append(i)
if len(aliquot) < k: #k번재 약수 없는 경우
    print(0)
    exit(0)
aliquot.sort()
print(aliquot[k-1])