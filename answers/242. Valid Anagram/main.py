"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings: s and t.
Return true if t is anagram of s else return false.

We should create a map of "s" and have a count for "s" length.
And loop through all the characters from "t".
Compare with the "s" map and remove from "s" count.
If "s" count is not equal to zero return false else true.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        sCount = len(s)
        for x in s:
            sMap[x] = sMap.get(x, 0) + 1
        for x in t:
            if sMap.get(x, 0) <= 0: return False
            sMap[x] -= 1
            sCount -= 1
        
        return True if sCount == 0 else False