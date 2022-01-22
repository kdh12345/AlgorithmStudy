import sys
import copy
numbers=list(map(int,sys.stdin.readline().split()))
while numbers!=[1,2,3,4,5]:
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
            for item in numbers:
                print(item,end=' ')
            print()
