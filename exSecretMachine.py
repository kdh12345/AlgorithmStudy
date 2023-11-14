import sys
n,m,k = map(int,sys.stdin.readline().split())
secret_arr   = ''.join(list(map(int,sys.stdin.readline().rstrip().split())))
machine_arr  = ''.join(list(map(int,sys.stdin.readline().rstrip().split())))


if secret_arr in machine_arr:
    print('secret')
else:
    print('normal')
