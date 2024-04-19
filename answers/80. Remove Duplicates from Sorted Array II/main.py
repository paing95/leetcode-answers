"""
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

we have integer array called "nums" in ascending order
members of the array can appear at least twice and
we will need to remove those that appear more than twice
when removing, we will need to keep the array members in initial order
meaning no ordering
at last we will need to return "k" which is valid elements
have to do in O(1) space

we should have a loop and an index called "k" and counter called "count"
inside the loop
    compare with previous element. if not the same, set "count" to 1.
    else add 1 to "count".
    then check the "count"
    if "count" is less than 3, put element to "k" index and plus one to "k"
don't check current one with previous element and the element before previous element
cos it will be a problem when putting element in "k" index and became 3 sequential elements
e.g. [1, 1, 1, 2, 2, 3] => [1, 1, 2, 2, 2, 3]
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        count = 0
        for i in range(len(nums)):
            if i == 0:
                count += 1
            else:
                if nums[i-1] == nums[i]:
                    count += 1
                else:
                    count = 1
            if count < 3:
                nums[k] = nums[i]
                k += 1

        return k