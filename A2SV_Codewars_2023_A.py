def find_smallest(a):
    a.sort()
    s = 1
    
    for num in a:
        if num <= s:
            s += num
        else:
            break
    return s

n = int(input())
a = list(map(int, input().split()))
print(find_smallest(a))