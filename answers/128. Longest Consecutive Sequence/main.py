"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

Given an unsorted integer array called "nums".
We are to find the length of longest consecutive elements sequence.
And have to find that length in O(n) time.

e.g. [100, 4, 200, 1, 3, 2]
We could sort the array first. [1, 2, 3, 4, 100, 200]
And we can do a loop to check if current item is previous item + 1.
And keep the count and maxCount.
If current item is not previous item + 1, reset the count.

OR

We could do a map, count each element in "nums".
Then, we will have a distinct keys() from the map.
After that, we can just loop the map keys and count.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums.sort()
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if i == 0:
                count += 1
                maxCount= 1
            else:
                if nums[i-1] + 1 == nums[i]:
                    count += 1
                elif nums[i-1] == nums[i]:
                    continue
                else:
                    maxCount = max(count, maxCount)
                    count = 1
        return max(count, maxCount)
        """

        if len(nums) < 2:
            return len(nums)
        
        numsMap = {}
        for num in nums:
            numsMap[num] = 1
        
        nums = sorted(list(numsMap.keys()))
        count, maxCount = 0, 0
        for i in range(len(nums)):
            if i == 0:
                count = 1
                maxCount = 1
            elif nums[i-1] + 1 == nums[i]:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 1
        return max(count, maxCount)