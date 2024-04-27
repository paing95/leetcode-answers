"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150

Given an integer array called "nums".
We need to return an integer array called "answer" and answer[i] is the product of all elements except from nums[i].
Need to finish in O(n).

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

how to solve?
if we do loop and multiply for initial and reverse order? let's try.

nums = [ 1, 2, 3, 4 ]

prefix for index 0: 1
postfix for index 0: 24

prefix for index 1: 1
postfix for index 1: 12

prefix for index 2: 2
postfix for index 2: 4

prefix for index 0: 6
postfix for index 0: 1

res = [1, 1, 1, 1]
we do a loop till len(nums) - 1
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= res[i]
        0 => res[i] = 1, prefix = 1
        1 => res[i] = 1, prefix = 2
        2 => res[i] = 2, prefix = 6
        3 => res[i] = 6, prefix = 24
    res = [ 1, 1, 2, 6 ]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        3 => res[3] = 6, postfix = 4
        2 => res[2] = 8, postfix = 12
        1 => res[1] = 12, postfix = 24
        0 => res[0] = 24, postfix = 24
    return res
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
