"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

Given a string "s".
We are to find longest sub string without repeating chars.
We should have a set to keep track of non-repeating chars.
We loop and add into the set until we find the repeating chars.
If we find a repeating char, we have to move left index 
until duplicate char no longer exists in the set.
And store the count.
Then continue.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        l, count = 0, 0
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            count = max(count, r - l + 1)
        
        return count