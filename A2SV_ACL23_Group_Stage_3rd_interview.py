"""
You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.

 

Example 1:

Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000
Example 2:

Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000
"""

import heapq
def station(stations, k):
    h = []
    n = len(stations)
    for i in range(1, n):
        d = stations[i] - stations[i-1]
        h.append((-d, d, 1))
    heapq.heapify(h)

    while k > 0:
        dis, total_dis, segment = heapq.heappop(h)
        dis *= -1
        second_dis = -h[0][0]
        m = max(0, ((total_dis - segment * second_dis) // second_dis) + 1)
        m = min(m, k)
        k -= m
        segment += m
        d = total_dis / segment
        heapq.heappush(h, (-d, total_dis, segment))
    return -h[0][0]

print(station([1,2,3,4,5,6,7,8,9,10],  9))
print(station([23,24,36,39,46,56,57,65,84,98], 1))


"""
After interview solution
import heapq
import math
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        n = len(stations)
        dis = [stations[i] - stations[i-1] for i in range(1, n)]
        dis.sort(reverse=True)

        def fun(d):
            c = 0
            for i in dis:
                m = int(math.ceil(i / d)) - 1
                c += m
                if c > k:
                    return False
            return True

        
        l = 0
        r = dis[0]
        M = 1e-6
        while abs(r-l) > M:
            m = (l + r) / 2
            if fun(m):
                r = m
            else:
                l = m
        return r
                

        

"""