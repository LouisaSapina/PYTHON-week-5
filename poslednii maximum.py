a = [int(x) for x in input(' Целые числа через пробел:').split()];
print(a)
m = max(a)
y = 0
for x in range(len(a)-1, 0, -1):
    if a[x] == m:
        y = x
        break
print(m, y)