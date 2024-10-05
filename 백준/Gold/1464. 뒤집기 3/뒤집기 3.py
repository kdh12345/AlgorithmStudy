import sys
input = sys.stdin.readline
from collections import deque

word = list(input().rstrip())
n = len(word)
def rev(l,r,arr):
    while l<r-1:
        tmp = arr[r-1]
        arr[r-1] = arr[l]
        arr[l] = tmp
        l += 1
        r -= 1
    return arr
for i in range(n-1):
      e = i+1
      if word[i] > word[e] and word[e] <= word[0]:
          rev(0,e,word)
          if word[i] >= word[e]:
              rev(0,e+1,word)


ans = ''.join(word)
print(ans)
