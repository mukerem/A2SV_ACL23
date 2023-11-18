def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1
    primes_list = [i for i in range(2, n + 1) if prime[i]]
    return primes_list


k, n = list(map(int, input().split()))
prizes = list(map(int, input().split()))
primes = sieve_of_eratosthenes(max(prizes))
if not primes:
    primes.append(int(1e9 + 7))
    
maxx = 0
for p in primes:
    s = 0
    c = 0
    for prize in prizes:
        if prize % p == 0:
            c += 1
        else:
            if prize + s <= k:
                s += prize
                c += 1
            else:
                break
    maxx = max(maxx, c)
print(maxx)

