import math
import sys

word = sys.stdin.readline().rstrip()
word_arr = word.split(':')
n = int(word_arr[0])
m = int(word_arr[1])
gcd_num = math.gcd(n,m)

n //= gcd_num
m //= gcd_num
print(n,end=':')
print(m)