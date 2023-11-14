i = 0
total = 0

for i in range(1,10+1,2):
    if i%2 and i%3:
        print(i)
        print(i%2,i%3)
        continue
    total+=i
print(total)