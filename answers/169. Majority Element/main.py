"""
169. Majority Element

For this question, we are given integer array called "nums" that has "n" size.
We will need to find the majority element that is included "n/2" times in the array.

[3, 2, 3],  Output is 3. How do we calculate this?

Let's have a "count" variable starts with 1 and a "major" variable assigned element at index 0.
And let's have a loop starting from index 1 to the end.
    inside the loop, we check if element at index "i" is the same as "major" variable.
    if it's the same, we plus one.
    else we minus one.
    then we check if "count" variable becomes 0. 
        if it becomes zero, we assign current element to "major" variable and assign 1 to "count" variable.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, major = 1, nums[0]
        for i in range(1, len(nums)):
            if major == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                major = nums[i]
        return major
