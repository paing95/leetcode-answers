"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

Given an ascending sorted integer array called "numbers".
And we have to find the indexes of two numbers those sum are target number.
Indexes must be added by one.
The trick here to find when to move left and right pointers.
We just need to move left pointer if target - right value is greater than left value.
If not, move right pointer.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < len(numbers) and r < len(numbers):
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif target - numbers[r] > numbers[l]:
                l += 1
            else:
                r -= 1