n, m = map(int, input().split())
pieces = map(int, input().split())


def solve(n, m, p):
    p = sorted(p)

    i = n-1
    j = 0
    dif = 1001
    while i < m:
        dif = min(dif, p[i]-p[j])
        i += 1
        j += 1
    return dif


print(solve(n, m, pieces))


