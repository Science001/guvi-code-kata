a, b = tuple(map(int, input().split(' ')))
fact = 1
for i in range(a, b, -1):
  fact *= i
print(fact)
