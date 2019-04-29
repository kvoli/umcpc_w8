n, wc, bc = map(int, input().split())
ds = input().split()


low_cost = min(wc, bc)
cost = 0

for i, d in enumerate(ds):
    dc = ds[n - i - 1]
    if d == '2':
        if dc == '0': cost += wc
        elif dc == '1': cost += bc
        else: cost += low_cost
    elif dc != '2' and d != dc:
        cost = -1
        break

print(cost)

