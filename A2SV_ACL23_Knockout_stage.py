"""
Given an integer array nums sorted in non-decreasing order and an integer k, 
return true if this array can be divided into one or 
more disjoint strictly increasing subsequences of length at least k, or false otherwise.

Example 1:
Input: nums = [1,2,2,3,3,4,4], k = 3
Output: true

Explanation: The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
1. The same numbers should not insert into the same subsequence because the numbers should be stricitly increasing i.e each numebrs in 1 subsequnce should be unique
2. First count the frequency of each numbers and assign maxx is the maximum frequency among all the numbers of let x
3. We should create at least maxx number of subsequnce because each x should be in different subsequence or group
4. n is the sizze of the original array, and we have at least maxx numebr of subsequence, so if we divide the k numbers into maxx number of subsequence, then we have 
   n / maxx elements in each subsequence. If the division return a float then it is like y = floor(n / maxx)
5. if y >= k then we should return True otherwise false  

Constrain
1 <= k <= nums.length <= 10**5
1 <= nums[i] <= 10**5
nums is sorted in non-decreasing order.

"""
def disjoint_count_2(arr, k):
    f = {}
    
    for i in arr:
        f[i] = f.get(i, 0) + 1
        
    maxx = max(list(f.values()))
    n = len(arr)
    size = n // maxx
    
    return size >= k

def disjoint_count(arr, k):
    n = len(arr)
    maxx = 1
    current = 1
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            current += 1
        else:
            maxx = max(maxx, current)
            current = 1
    maxx = max(maxx, current)
    size = n // maxx
    return size >= k

print(disjoint_count([1,2,2,3,3,4,4], 3))
"""
Time complexity - O(n)
Space complexity - O(1)
"""