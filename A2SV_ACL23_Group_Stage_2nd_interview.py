"""
Given an integer array nums, return the number of non-empty subarrays with the leftmost element of the subarray not larger than other elements in the subarray.
A subarray is a contiguous part of an array.
 
Example 1:
Input: nums = [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].

Example 2:
Input: nums = [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].

Example 3:
Input: nums = [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].

###################
nums = [1,4,2,5,3]
stack = []
iteration 1 -> stack = [1]
iteration 2 -> stack = [1, 4]
iteration 3 -> we should remove the number 4 so that indicate [4] satisfy the given condition and we should add 2 in to the stack => [1, 2]
iteration 4 -> stack = [1, 2, 5]
itertaion 5 -> we should remove 5, [5] is one of the possible subarray. we should also add 3, so the stack become [1, 2, 3]
x and the next element is y, n = (y-x+1), so we have to n * n(-1) / 2 subarray
in each iteration 


a1, a2, a3, ... an
a1 <= a2, a1 <= a3, ..., a1 <= an

"""
def subarray(arr):
    n = len(arr)
    stack = []
    count = 0
    for idx, v in enumerate(arr):
        while stack and v < stack[-1][0]:
            top, i = stack.pop()
            count += (idx - i)
        else:
            stack.append((v, idx))
    for _, i in stack:
        count += (n - i)
        
    return count
print(subarray([1,4,2,5,3]))
print(subarray([2,2,2]))
        
# https://sharepad.io/live/o1Qoy0W