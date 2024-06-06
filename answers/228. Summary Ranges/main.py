"""
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

Given a sorted unique integer array called "nums".
We are to find all the ranges within the array.
e.g. nums = [0,1,2,4,5,7] => ["0->2","4->5", "7]

We could use two arrays: one to remember end results and another to remember current range.
We do a simple for loop throuh nums.
And check
1. if current element is previous element + 1 then append to current_arr
2. if we are at end of array and current element is previous element + 1, append current_arr to final_arr
3. if we are at end of array and current element is not previous element + 1, 
    we append current_arr first to final_arr
    then we append current element to final_arr
4. if we are at neither the start nor the end and current element is not previous element + 1,
    we append current_arr to final_arr
    then reset current_arr
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1: return [ str(nums[0]) ]

        tmp, res = [], []
        for i in range(len(nums)):
            if i == 0 or nums[i-1] + 1 == nums[i]:
                tmp.append(nums[i])
            
            if i == len(nums) - 1 and nums[i-1] + 1 == nums[i]:
                res.append("{0}->{1}".format(tmp[0], tmp[-1]))
            
            elif i == len(nums) - 1 and nums[i-1] + 1 != nums[i]:
                if len(tmp) == 1:
                    res.append(str( tmp[0] ))
                else:
                    res.append("{0}->{1}".format(tmp[0], tmp[-1]))
                
                res.append(str( nums[i] ))
            
            elif 0 < i and i < len(nums) - 1 and nums[i-1] + 1 != nums[i]:
                if len(tmp) == 1:
                    res.append(str( tmp[0] ))
                else:
                    res.append("{0}->{1}".format(tmp[0], tmp[-1]))
                tmp = [nums[i]]
        return res
