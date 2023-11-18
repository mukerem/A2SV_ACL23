
def solve():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    import bisect
    ans = 0
    for i in b:
        x = bisect.bisect_left(a, i)
        y = x - 1 if x > 1 else 0
        z = a[x] - i if x < len(a) else 1e9
        z = min(i - a[y], z)
        ans = max(ans, z)
    print(ans)
solve()