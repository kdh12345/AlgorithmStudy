
t = int(input())
stu = list(map(int,input().split()))
st = []
num = 1
while len(stu) > 0:
    if stu[0] == num:
        stu.pop(0)
        num += 1
    else:
        st.append(stu.pop(0))

    while st:
        if st[-1] == num:
            st.pop()
            num += 1
        else:
            break

if len(st) == 0:
    print('Nice')
else:
    print('Sad')

"""for i in range(len(stu)):
    if num < stu[i]:
        st.append(stu[i])
    else:
        result.append(stu[i])
        #st.pop()
        num += 1

while len(st) > 0:
    result.append(st[-1])
    st.pop()

isNot = False
for i in range(t):
    if result[i] == i+1:
        isNot = True
    else:
        isNot = False
        break

if isNot == True:
    print('Nice')
else:
    print('Sad')
"""