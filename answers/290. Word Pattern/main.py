"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings: pattern, s
And we are to check if string "s" follows the string "pattern".
if we are to loop through string "s".
and split the string spaces to each word.
if next char of "s" is a space or if we reach end of string
we should check if the word already exists in our "s" map.
if not, we should check if current index of "pattern" already exists in "pattern" map.
if so, return False.
else continue to add into both "s" and "pattern" maps.
then add into a final string.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # simpler version
        words = s.split(' ')
        wordMap, patternMap = {}, {}
        finalStr = ""
        i = 0
        for word in words:
            if i >= len(pattern): return False

            p = wordMap.get(word, "")
            if not p:
                if patternMap.get(pattern[i], ""): return False
                wordMap[word] = pattern[i]
                patternMap[pattern[i]] = word
            i += 1
            finalStr += wordMap[word]
        return True if finalStr == pattern else False

        # no manual split version
        sMap, patternMap = {}, {}
        myStr, myPattern = "", ""
        j = 0
        for i in range(len(s)):
            if j >= len(pattern): return False

            if s[i] != " ":
                myStr += s[i]
            
            # if next index of s is a space or if we reach end of string
            if (i < len(s) - 1 and s[ i+1 ] == " ") or (i+1 == len(s)):
                # if no value in the map
                # check if j index of pattern is already in patternMap
                if not sMap.get(myStr, ""):
                    # pattern[j] => a
                    if patternMap.get(pattern[j], "") and patternMap.get(pattern[j], "") != myStr:
                        return False
                    sMap[ myStr ] = pattern[j]
                    patternMap[ pattern[j] ] = myStr
                
                j += 1
                myPattern += sMap[ myStr ]
                myStr = ""

        return True if myPattern == pattern else False