"""
15. 3Sum
https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

We are given an integer array called "nums".
And we have to return one or more sets of three values that sum up to 0.

Sorting the array so that we could use left and right pointer
to transform the problem to two sums.

While looping, we could skip the nums[i] if it's the same as nums[i-1].
Same goes for left pointer.
Why? Cos combinations have to be unique.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([ nums[i], nums[j], nums[k] ])

                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res