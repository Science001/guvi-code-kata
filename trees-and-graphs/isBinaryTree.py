n, k = tuple(map(int, input().split(' ')))
children = set()
roots = dict()
maxCount = 0
for i in range(k):
  a, b = tuple(map(int, input().split(' ')))
  children.add(b)
  if(a in roots):
    roots[a] += 1
  else:
    roots[a] = 1
  if(roots[a] > maxCount):
    maxCount = roots[a]
if(len(children) == n-1 and maxCount <= 2):
  print("YES")
else:
  print("NO")
