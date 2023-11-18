"""
You are given a 1-indexed array nums of n integers.
A set of numbers is complete if the product of every pair of its elements is a perfect square.
For a subset of the indices set {1, 2, ..., n} represented as {i1, i2, ..., ik}, we define its element-sum as: nums[i1] + nums[i2] + ... + nums[ik].
Return the maximum element-sum of a complete subset of the indices set {1, 2, ..., n}.
A perfect square is a number that can be expressed as the product of an integer by itself.

Example 1:
Input: nums = [8,7,3,5,7,2,4,9]
Output: 16
Explanation: Apart from the subsets consisting of a single index, there are two other complete subsets of indices: {1,4} and {2,8}.
The sum of the elements corresponding to indices 1 and 4 is equal to nums[1] + nums[4] = 8 + 5 = 13.
The sum of the elements corresponding to indices 2 and 8 is equal to nums[2] + nums[8] = 7 + 9 = 16.
Hence, the maximum element-sum of a complete subset of indices is 16.

s = (a1, a2, ..., an)
a1 * a2 = perfect square
a1 * a3 = perfect 

1 - (1, 4, 9, 16, ...,) x^2, y^2 if we multiply (x*y)^2
2 - (x, x^3, x^5, ...) x^a * x^b = x ^(a+b)

(2, 2^3, 2^5,...)
"""

def complete_subset(arr):
    n = len(arr)
    ans = [0] * (n+1)
    s = int(n ** .5)
    for i in range(1, s + 1):
        idx = i * i - 1
        ans[1] += arr[idx]
    for i in range(2, s+1):
        idx = i
        while idx <= n:
            ans[i] += arr[idx-1]
            idx *= i * i
    return max(max(ans), max(arr))
print(complete_subset([8,7,3,5,7,2,4,9]))
print(complete_subset([5,10,3,10,1,13,7,9,4]))

#
"""
Time complexity - O(n)
Space complexity - O(n)
"""