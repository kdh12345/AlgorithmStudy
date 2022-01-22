import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().split()))
arr_t=list(sorted(set(arr)))
arr_t={arr_t[i]:i for i in range(len(arr_t))}
print(*[arr_t[i] for i in arr]) #해당 값이 전체 집합에서 몇 번째로 낮은 숫자인지를 반환하는 것