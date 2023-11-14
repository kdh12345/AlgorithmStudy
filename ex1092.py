import sys
n = int(sys.stdin.readline().rstrip())
cranes = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
boxes = list(map(int,sys.stdin.readline().split()))

boxes.sort(reverse= True)
cranes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    exit(0)

answer = 0
while boxes:

    for i in range(len(cranes)):
         for j in range(len(boxes)):
             if cranes[i] >= boxes[j]:
                boxes.pop(j)
                break
    answer += 1


print(answer)
