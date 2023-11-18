def solve():
    n, x, y = map(int, input().split())
    x, y = max(x, y), min(x, y)
    # if n == 1:
    #     print(0)
    #     return
    
    u = x * (n-1)
    v = (x + y)
    if u % v == 0:
        b1 = b2 = u // v
    else:
        b1 = u // v
        b2 = b1 + 1

    a1 = n - 1 - b1
    a2 = n - 1 - b2

    if max(a1 * x, b1 * y) <= max(a2 * x, b2 * y):
        print(y + max(a1 * x, b1 * y))
    else:
        print(y + max(a2 * x, b2 * y))

# def solve():
#     n, x, y = map(int, input().split())
#     x, y = min(x, y), max(x, y)
#     # if n == 1:
#     #     print(0)
#     #     return
#     l = 1
#     r = x * n
#     while l < r:
#         m = (l + r) // 2
#         a = m - x
#         copy = 1 + a // x + a // y
#         if copy < n:
#             l = m + 1
#         else:
#             r = m
#     print(l)
solve()