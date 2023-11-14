arr = [
  [1,2],
  [2,3],
  [2,4],
  [2,5],
  [5,6],
  [5,7],
  [6,8],
  [2,9]
]
graph = [[] for _ in range(len(arr)+1)]

for a in arr:
    graph[a[0]].append(a[1])

