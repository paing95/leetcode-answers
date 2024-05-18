"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings: "s" and "t".
We have to find minimum possible substring of "s" that has all the characters in "t".
Substring can contain multiple occurrences of "t" elements.

The trick here is to 
1. use a map to keep track of char occurrences
2. keep shifting the left index until the substring has all "t" elements

Two cases that may be solved before main codes:
1. if "s" and "t" are the same, we can return "s" or "t"
2. if length of "t" is greater than that of "s", there is no possible substring so we can return blank string

E.g. s = "aabbcc", t = "aabc"
In here, "t" only has one occurrence of "a", "b", "c".

Count of T
a => 2 => 1 condition
b => 1 => 1 condition
c => 1 => 1 condition

As long as we satisfy those three conditions in the sub string, we need to keep adding/removing the chars in substring.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
            window[char] = 0

        l = 0
        res, resLen = [-1, -1], len(s) + 1
        need, have = len(countT), 0

        for r in range( len(s) ):

            if s[r] in window: window[ s[r] ] += 1
            if s[r] in window and window [ s[r] ] == countT[ s[r] ]: have += 1

            while have == need and l <= r:
                if resLen > (r - l + 1):
                    res = [l, r]
                    resLen = r - l + 1
                
                if s[l] in window: window[ s[l] ] -= 1
                if s[l] in window and window [ s[l] ] < countT[ s[l] ]: have -= 1

                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != len(s) + 1 else ""