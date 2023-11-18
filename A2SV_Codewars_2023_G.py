def solve():
    M = int(1e9) + 7
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    pascal = [[1]* n for i in range(n)]
    for i in range(1, n):
        for j in range(1, i):
            pascal[i][j] = (pascal[i-1][j-1] + pascal[i-1][j]) % M
    
    cof = pascal[-1]
    prefix = []
    t = 0
    for i in cof:
        t += i
        t = t % M
        prefix.append(t)
    prefix.append(0)
    top = 0
    for i in range(n):
        top += (a[i] * cof[i])
        top = top % M
    # print(top, cof)
    for i in range(q):
        l, r, v = map(int, input().split())
        add = prefix[r] - prefix[l-1]
        add = (add * v) % M
        top = (top + add) % M
        print(top)
    

solve()