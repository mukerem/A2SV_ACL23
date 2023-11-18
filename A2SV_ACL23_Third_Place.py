"""
nums = [1,2,3,10] - > [1,5,1] -> operations = 1 [16] ->3
      
[1, 2, 3, 10]
l = 0, r = 3
[1, 3, 3, 10] l = 1, r = 3
[1, 3, 6, 10] l = 2, r = 3
[1, 3, 16, 10] l = 3, r  = 3
[4,3,2,1,2,3,1] l = 0, r = 6 counter = 0
[4,3,2,1,2,4,1] l = 0, r = 5 counter = 1
[4,3,2,1,2,4,1] l = 1, r = 4 counter = 1
[4,3,2,3,2,4,1] l = 1, r = 3 counter = 2
[4,3,2,3,2,4,1] l = 2, r = 2 counter = 2

1. inintialize left = 0, right = n-1, merge = 0
2. check the values at left and right if both are the same then left += 1 and right -= 1
3. else merge +=1 and move the pointer which have smallest value and merge in that index
4. Increase the merge count by 1 if they are not equal
5. iterate until left < right

"""

def minimumOperations(nums) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    merge = 0
    
    while left < right:
        if nums[left] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] < nums[right]:
            left += 1
            nums[left] += nums[left - 1]
            merge += 1
        else:
            right -= 1
            nums[right] += nums[right + 1]
            merge += 1
    return merge

print(minimumOperations([1,2,3,1]))

"""
Time complexity - O(n)
Space complexity - O(1)
"""

# https://sharepad.io/live/KJwYcqd