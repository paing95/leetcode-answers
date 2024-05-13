"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

Given an integer array height.
The two endpoints of the ith line are (i, 0) and (i, height[i]).
Which means x is 0 and y is height[i].
We will need to find most water a container of two walls (height[x] and height[y]).

Let's have a left and right pointers l and r.
let's have a total that stores the value.
l = 0, r = len(height) - 1
we loop until l < r
while l < r:
    tmp = height[r] if height[l] > height[r] else height[l]
    total = max(total, tmp * (r-l))
    
    conditions to move left pointer
    if height[l] < height[r]: l += 1
    else: r -= 1

We could make processing faster for the array that has two elements.
Be careful not to multiply height * height.
We are to multiply height * (r-l)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, total = 0, len(height) - 1, 0
        while l < r:
            tmp = height[r] if height[l] > height[r] else height[l]
            total = max(total, tmp * (r - l))

            if height[l] < height[r]: l += 1
            else: r -= 1
        
        return total