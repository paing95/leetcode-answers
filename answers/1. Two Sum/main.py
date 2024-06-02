"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

Given a integer array "nums" and we have to find the integer "target" that is the sum of two numbers.
Finally, we should return the indexes of two numbers.

--- if array is sorted ---
We should have two pointers - left and right.
left at the start, right at the end.
We should keep moving the pointers
if left + right: return [left, right]
elif right > target: right pointer - 1
else: left pointer - 1

--- if array is not sorted ---
We should have a hashmap called "numMap".
And we should loop through the "nums" array.
Inside the loop,
we should add current number inside the map as part of an array.
And we should check for another number (target - current number).
After that, we should check if another number is same as current number.
And if the current number array in the map has more than one element, return first two elements.
If another number is different from current number, we should return first element of two numbers from the map.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            current_array = numMap.get(nums[i], [])
            current_array.append(i)
            numMap[nums[i]] = current_array

            another_num = target - nums[i]
            if another_num == nums[i] and len(numMap[nums[i]]) > 1:
                return numMap[nums[i]][:2]
            elif another_num != nums[i] and another_num in numMap:
                return sorted( [ numMap[ nums[i] ][0], numMap[another_num][0]] )
        return []