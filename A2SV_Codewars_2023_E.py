def solve():
    n, m, s, a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    x = []
    t = 0
    for i in range(min(n, s // a)):
        t += A[i]
        x.append(t)

    y = []
    t = 0
    for i in range(min(m, s // b)):
        t += B[i]
        y.append(t)

    if not x and not y:
        print(0)
        return
    if not x:
        print(y[-1])
        return
    if not y:
        print(x[-1])
        return

    
    maxx = max(y[-1], x[-1])
    l = 1
    r = len(y)
    t = 0
    while r > 0 and l <= len(x):
        while l <= len(x) and l * a + r * b  <= s:
            maxx = max(maxx, x[l-1] + y[r-1])
            l += 1
        r -= 1
    print(maxx)


solve()