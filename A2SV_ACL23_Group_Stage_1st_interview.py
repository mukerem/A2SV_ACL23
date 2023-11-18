"""
You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.
The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.
Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.


Input: image = [["0","0","1","0"]
                ["0","1","1","0"]
                ["0","1","0","0"]], x = 0, y = 2
Output: 6
Input: image = [["1"]], x = 0, y = 0
Output: 1


["0","0","1","0"],
["0","1","1","0"],
["0","1","0","0"]

Follow Up question
You must write an algorithm with less than O(mn) runtime complexity
"""
def smallest_area(arr, x, y):
    m = len(arr)
    n = len(arr[0])

    def check_all_white_horizontal(idx):
        for i in arr[idx]:
            if i == "1":
                return False
        return True

    def check_all_white_vertical(idx):
        for row in arr:
            if row[idx] == "1":
                return False
        return True 

    def binary_search_vertical_top(l, r):

        while l < r:
            m = (l + r) // 2
            if check_all_white_horizontal(m):
                l = m + 1
            else:
                r = m
        return l

    def binary_search_vertical_bottom(l, r):

        while l < r:
            m = (l + r) // 2
            if check_all_white_horizontal(m):
                r = m - 1
            else:
                l = m
        return l 


    def binary_search_horizontal_left(l, r):

        while l < r:
            m = (l + r) // 2
            if check_all_white_vertical(m):
                l = m + 1
            else:
                r = m
        return l

    def binary_search_horizontal_right(l, r):

        while l < r:
            m = (l + r) // 2
            if check_all_white_vertical(m):
                r = m - 1
            else:
                l = m
        return l 

    x1 = binary_search_vertical_top(arr, 0, x)
    x2 = binary_search_vertical_bottom(arr, x, m-1)
    y1 = binary_search_horizontal_left(arr, 0, y)
    y2 = binary_search_horizontal_right(arr, y, n-1)
    return (x2-x1 + 1) * (y2-y1+1)


# https://sharepad.io/live/1pZDIP3