def odd_median(a, n):
    ans = abs(a[n // 2] - a[(n // 2) - 1])
    return ans

def even_median(a, n):
    ans = abs(a[n // 2] + a[(n // 2) - 1] - a[n // 2 + 1] - a[(n // 2) - 2]) / 2
    return ans

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 4 == 2:
        print(odd_median(a, n))
    else:
        print(even_median(a, n))
solve()