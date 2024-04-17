"""
26. Remove Duplicates from Sorted Array

we have integer array nums that is already sorted in ascending order
we will need to remove any duplicates however will need to keep elements in initial order
instead of using a new array, we will need to have k elements of the array be unique

we will have a loop and an index(k) to keep track of unique elements
we could either check next or previous element of current index
easier and suitable way is to check if previous element is same as current element
if same, skip else put the element on the index and increase the index
loop will finish in O(n)
don't forget to start k as 1
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

