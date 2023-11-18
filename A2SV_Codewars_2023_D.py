def solve():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    repeat = p // s
    p = p % s
    idx = 0
    minn = n
    for i in range(n):
        c = 0
        j = 0
        while c < p:
            c += a[(i+j)%n]
            j += 1
        if j < minn:
            minn = j
            idx = i
    print(idx+1, repeat * n + minn)
solve()