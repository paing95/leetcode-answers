"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings: ransomNote and magazine
We are to check if "ransomNote" can be constructed using chars from "magazine".
Return true if it is true else false.

Rule: Each char in "magazine" can only be used once in "ransomNote".

Let's create a map for each char in "magazine".
And we just loop through "ransomNote" and
1. check if current char in the map
2. if it is in the map and check whether still have char left.

Based on those conditions, return true or false.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = {}
        for x in range(len(magazine)):
            magazineMap[magazine[x]] = magazineMap.get(magazine[x], 0) + 1
        
        for x in range(len(ransomNote)):
            # if char is not in map or becomes zero
            if magazineMap.get(ransomNote[x], 0) == 0: return False
            magazineMap[ransomNote[x]] -= 1
        
        return True