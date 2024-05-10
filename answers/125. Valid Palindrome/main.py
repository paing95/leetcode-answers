"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

We are given a string and we have to check if the string could be a palindrome.

A palindrome is a string with lowercase chars without non-alphanumeric chars that reads the same forward and backward.

Returns true if string is palindrome else false.
"""
class Solution:
    def is_char_allowed(self, value):
        if ord(value.lower()) >= ord("a") and ord(value.lower()) <= ord("z"):
            return True
        elif ord(value.lower()) >= ord("0") and ord(value.lower()) <= ord("9"):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        forward, backward = "", ""
        i, j = 0, len(s) - 1
        while i < len(s):
            # we could use isalnum or our own method is_char_allowed
            if s[i].lower().isalnum():
                forward += s[i].lower()
            
            if s[j].lower().isalnum():
                backward += s[j].lower()
            
            i += 1
            j -= 1
        
        return True if forward == backward else False