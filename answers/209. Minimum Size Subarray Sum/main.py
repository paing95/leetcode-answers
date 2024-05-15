"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

Given a positive integer array called "nums" and a positive integer
called "target".
We are to return min length of sub array which sum is >= target.
        
If we sort the array first, it'll be easier to count from behind.
But note that we cannot sort the array as we have to count subarray.
Also sub array can start from any index of the array so
starting simultaneously from furthest left and furthest right will not work.

We will have to use sliding window method.
e.g. [2, 3, 1, 2, 4, 3]
l, r = 0, 0
sum of l to r is 1. still less than target
so we have to shift right.

l, r = 0, 1
sum of l to r is 5. still less than target
so we have to shift right.

l, r = 0, 2
sum of l to r is 6. still less than target
so we have to shift right.

l, r = 0, 3
sum of l to r is 8. larger than target
so we have to shift left.

and so on till l and r are out of bounds
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total, count = 0, 0, target + 1
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                count = min(count, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if count == target + 1 else count
