"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

Given a string "s". We are to count the length of last word.
s = " Hello World " => count is 5

We are to ignore the the spaces that comes before last word.

We could use the method strip() and count from behind till we hit a space.
OR
We could count from behind. Skipping spaces.

Either way, it will work.

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.strip()

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            
            count += 1
        return count

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        hit = False
        stop = False
        i = len(s) - 1
        count = 0
        while not stop:
            if (hit and s[i] == " ") or i == 0:
                stop = True
            if not hit and s[i] != " ":
                hit = True
            
            if hit and s[i] != " ":
                count += 1
            i -= 1
        return count