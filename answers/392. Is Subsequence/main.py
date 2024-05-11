"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

Given two strings: s, t
We need to find out whether s is a subsequence of t.

e.g. "ace" is a subsequence of "abcde"
"aec" is not a subsequence of "abcde"

From the looks of it, subsequence needs to be in order.
Every char in "aec" is in "abcde". however, they are out of order.

Edge cases: 
1. if len(s) is greater than len(t): false
2. if s is equal to t, true

We should do a while loop with two indexes: x, y
until we runs out of len(s)
        
Inside the loop, when we reach len(s) -1, should return true
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s has more chars than t
        if len(s) > len(t): return False
        # if both strings are the same
        if s == t: return True

        x, y = 0, 0
        while x < len(s) and y < len(t):
            if s[x] == t[y]:
                x += 1
                y += 1
            else:
                y += 1

        if x != len(s):
            return False
        else: 
            return True
