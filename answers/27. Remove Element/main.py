"""
27. Remove Element
https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

we have integer array "nums" and integer "val"
and we need to remove all the "val" integers from the array "num"
and return the number of elements that are not "val" i.e. first k elements
should be integers that are not "val".

so we will probably need an index to keep track of integers that are not "val"
let's call it k
we should probably have a loop
    inside the loop if array[index] is not "val"
        we put array[k] = array[index]
        k += 1
    that way we use the loop index and k properly and will finish in O(n) time.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[k] = nums[index]
                k += 1
        return k