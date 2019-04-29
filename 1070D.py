n, k = map(int, input().split())
a = [int(x) for x in input().split()]

bags, r = 0, 0

for i in range(n):
    x = a[i] + r
    if x == 0:
        continue
    elif x < k and r > 0:
        bags += 1
        r = 0
    else:
        bags += (x // k)
        r = (x % k)

if r > 0:
    bags += 1

print(bags)

