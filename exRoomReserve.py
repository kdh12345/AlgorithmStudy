import sys
n,m = map(int,sys.stdin.readline().split())
rooms = dict()
for _ in range(n):
    room_name = sys.stdin.readline().strip()
    rooms[room_name] = [[i,i+1] for i in range(9,18)]
reserved_rooms = []
for _ in range(m):
    arr = sys.stdin.readline().split()
    room      = arr[0]
    startTime = arr[1]
    endTime   = arr[2]
    for i in range(int(startTime),int(endTime)):
        if [i,i+1] not in rooms[room]:
            continue
        else:
            rooms[room].remove([i,i+1])

for v in sorted(rooms.keys()):
    if len(rooms[v]) == 0:
        print("Room "+ v + ":")
        print("Not available")

        if v == sorted(rooms.keys())[-1]:
            break
        else:
            print("-----")
        continue
    else:
        temp = []
        ans = []

        for i in range(len(rooms[v])):
            if len(rooms[v]) == 1:
                temp.append(rooms[v][i])
            if i == len(rooms[v])-1:
                temp.append(rooms[v][i])
            elif 0<=i< len(rooms[v])-1:
                if rooms[v][i][1] == rooms[v][i+1][0]:
                    temp.append(rooms[v][i])
                else:
                    temp.append(rooms[v][i])
                    ans.append([temp[0][0], temp[-1][1]])
                    temp = []
        if temp == []:
            continue
        else:
            ans.append([temp[0][0],temp[-1][1]])

        print("Room " + v + ":")
        print(len(ans), "available")
        for i in range(len(ans)):
            if ans[i][0] == 9:
                ans[i][0] = '09'
                print(str(ans[i][0])+"-"+str(ans[i][1]))
            else:
                print(str(ans[i][0])+"-"+str(ans[i][1]))
        if v == sorted(rooms.keys())[-1]:
            break
        else:
            print('-----')
