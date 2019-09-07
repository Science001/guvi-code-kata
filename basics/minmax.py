n = int(input())
values = list(map(int, input().split(' ')))
mini = maxi = 0
for i in range(1, n):
  if(values[i] < values[mini]):
    mini = i
  elif(values[i] > values[maxi]):
    maxi = i
print("%d %d" % (mini+1, maxi+1))
