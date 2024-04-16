"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums1 and nums2 are in ascending order.
m = len(nums1), n = len(nums2)
merge nums1 and nums2 in a single array in ascending order.
instead of returning merged array, put the merged result in nums1.
nums1 has the length of m + n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

how do we solve this?

we will need an index to keep track of merged array which is still nums1.
let's call it k.

index for nums1. let's call it i.
index for nums2. let's call it j.

it's easier to start working from the end.
i = m - 1
j = n - 1
k = m + n - 1

and we keep reducing index by 1 on each loop.

let's have a while loop k >= 0: cos on last step, k will be zero.
    so how do we compare?
    let's clear our the known edge cases: runs out of nums1, runs out of nums2
    so if i < 0: which means we run out of nums1 elements,
        just put nums2[j] in nums1[k]
    else if j < 0: which means we run out of nums1 elements,
        just put nums2[j] in nums1[k] 
    else if nums1[i] > nums2[j]:
        just put nums1[i] in nums1[k]
    else:
        just put nums2[j] in nums1[k]

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while k >= 0:
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1