"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array "nums" and positive integer "k" to rotate the array "nums" to the right.
e.g. nums = [1,2,3,4,5,6,7], k = 3, Output => [5,6,7,1,2,3,4]

so how do we solve this? if we do brute force, it will be hard as hell to do 
as all members of the array have to move at the same time.

instead of shifting one element at a time, let's try rotating the whole array.
[1,2,3,4,5,6,7] => [7,6,5,4,3,2,1]
if we compare the output [5,6,7,1,2,3,4] with rotated array [7,6,5,4,3,2,1]
we could see the first 3 elements of the rotated array is just reverse order of first 3 members of the output array.
similarly, the last 4 elements of the rotated array is just reverse order of last 4 members of the output array.
so basically if we are to rotate 3 times, we will get the desired output.
1. rotate the whole array
2. rotate first "k" elements of the rotated array
3. rotate remaining elements of the rotated array
notice that k could be 0 to 10 ^ 5 so it will be smart to take the remainder of k divided by length of array "nums". 
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1