"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

We are given a string "s" and we are to reverse the string.
And we have to 
1. Do not include any leading or trailing spaces.
2. Must only include one space between each word.

E.g. 
Input: s = "  the sky   is blue  "
Output: "blue is sky the"

We could first strip the "s" string.
By that way, we do not have to care about leading or trailing spaces.

variables called output and tmpStr
After that, we could loop from the end of the string.
    when we reach end of string and tmpStr is not empty
        append tmpStr to output
    
    when we encounter a space and tmpStr is not empty
        append tmpStr to output
    
    if we output already has a space. stop appending spaces.
    
    when we encounter not a space, we should put inside tmpStr
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        output, tmpStr = "", ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                tmpStr = s[i] + tmpStr
            # conditions to add tmpStr
            # when we encounter a space and tmpStr is not empty
            if s[i] == " " and tmpStr:
                if output: output = output + " " + tmpStr
                # this is for the very first word
                else: output = tmpStr
                tmpStr = ""
            # or when we reach end of s
            elif i == 0 and tmpStr:
                if output: output = output + " " + tmpStr
                # this is if s has only one word
                else: output = tmpStr

        return output