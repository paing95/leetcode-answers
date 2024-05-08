"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150

We are given two strings "needle" and "haystack".
And we have to search "needle" in "haystack".
And return first occurrence of "needle" or -1 if not present.

let's use an index to keep track of "haystack".
And we loop the "haystack"
    while i < len(haystack):
        if haystack[i] != needle[0]:
            i += 1
            continue
        
        for x in range(1, len(needle)):
            if haystack[i + x] != needle[x]:
                break

            if haystack[i + x] == needle[x] and x + 1 == len(needle):
                return i
        i += 1
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # edge case if haystack = needle
        if haystack == needle: return 0
        # edge case if len(needle) > len(haystack):
        if len(needle) > len(haystack): return -1
        
        i = 0
        while i < len(haystack):
            if haystack[i] != needle[0]:
                # no point continuing if i + len(needle) is bigger
                if i + len(needle) > len(haystack): break
                i += 1
                continue

            # edge case if at last index and no more need to check
            if len(needle) == 1: return i
            for x in range(1, len(needle)):
                if i + x >= len(haystack): break
                
                if haystack[i + x] != needle[x]:
                    break
                if haystack[i + x] == needle[x] and x + 1 == len(needle):
                    return i
            
            i += 1
        
        return -1
