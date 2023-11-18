"""

You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively.
The warehouse's rooms are labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.
    
    Boxes are put into the warehouse by the following rules:
    Boxes cannot be stacked.
    You can rearrange the insertion order of the boxes.
    Boxes can be pushed into the warehouse from either side (left or right)
    
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped
before that room.
Return the maximum number of boxes you can put into the warehouse.


Constraints:
    n == warehouse.length
    1 <= boxes.length, warehouse.length <= 10^5
    1 <= boxes[i], warehouse[i] <= 10^9

Example 1:
Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
Output: 4

 I sorted the box
1. I store the maximum possible height to insert in index i from left and right (i.e left, right)
   It is increasing array upto the heighest pick value then it is decresing
2. Then I select the maximum from both arrays, max_height, idx
3. Then find the box which have a nearest height and it should less than that max_height
4. two pointers like l = idx -1 , r = idx + 1
5. I should insert by using two pointers

"""

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        n = len(warehouse)
        
        left = [0] * n
        right = [0] * n
        minn = float("inf")
        for i in range(n):
            minn = min(minn, warehouse[i])
            left[i] = minn
        minn = float("inf")
        for i in range(n-1, -1, -1):
            minn = min(minn, warehouse[i])
            right[i] = minn
        maxx = max(max(left), max(right))
        idx = None
        for i, v in enumerate(left):
            if maxx == v:
                idx = i
                break
        for i, v in enumerate(right):
            if maxx == v:
                idx = i
                break
        l = idx - 1
        r = idx + 1
        count = 0
        boxes.sort()
        index = bisect.bisect_right(boxes, maxx) - 1
        if index == 0:
            return 0
        count += 1
        index -= 1
        while l >= 0 and r < n and index >= 0:
            v = boxes[index]
            if left[l] >= v:
                count += 1
                l -= 1
            elif right[r] >= v:
                r += 1
                count += 1
            index -= 1
        
        return count
    
# https://sharepad.io/live/tA2f4Rw