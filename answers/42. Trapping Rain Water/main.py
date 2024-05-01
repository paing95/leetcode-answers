"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

how to get trap water?
the trip here to get max left and max value.
*
*        *
*        *
*        *
left    right
And get the min of those two values and subtract the current height.
left => 4, right => 3, current => 0, min(left, right) => 3, 3-0 => 3


3                                *
2                *                   *       *
1        *           *       *           *       *
0    *       *           *
     0   1   2   3   4   5   6   7   8   9   10  11

let's have a maxLeft, maxRight = height[0], height[len(height) - 1]
we compare left and right at each loop.

first => index 0 for the left, index 11 for the right.
left is 0, right is 1, since left < right, we move l += 1.
then update maxLeft to 1. water available = maxleft - current value => 1 - 1 => 0

second => index 1 for the left, index 11 for the right.
left is 1, right is 1, since left >= right, we move l -= 1.
then update maxRight to 2. water available = maxRight - current value => 2 - 2 => 0

third => index 1 for the left, index 10 for the right.
left is 1, right is 2, since left < right, we move l + 1
then keep maxLeft to 1. water available = maxleft - current value => 1 - 0 => 1
why maxleft - current value, cos we are moving l pointer as maxLeft is smaller than maxRight
water will spill if it's bigger than smallest value.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        water = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
        return water