"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array "nums" and an integer "k"
We are to return "true" if two different indexes "i" and "j" in array such that
nums[i] == nums[j] and abs(i-j) <= k.

We should create a hashmap "myMap".
We loop through "nums" and check if nums[i] in "myMap".
If it is in "myMap", check if current index - last index <= k. return true.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}
        for i in range(len(nums)):
            if nums[i] in myMap:
                if abs(myMap[nums[i]][-1] - i) <= k:
                    return True
            
            myMap[ nums[i] ] = myMap.get(nums[i], [])
            myMap[ nums[i] ].append(i)
        
        return False