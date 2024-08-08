t = int(input())
for _ in range(t):
    n,m,k,d = map(int,input().split())
    b = 2*d//(k*n*m*(m-1) + m*m*n*(n-1))
    if b == 0:
        print(-1)
    else:
        print(m*(m-1)*n*k*b//2 + m*m*n*(n-1)*b//2)
