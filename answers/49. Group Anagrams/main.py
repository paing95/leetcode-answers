"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

Given a string array "strs" and we are to group the anagrams together.
And return an array of group anagram arrays.

We should create a dict first "myMap".
And we loop through the array "strs" and sort each word.
Check if exists in "myMap", append if exists else create new key: value array.
Finally return the values of "myMap".
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for word in strs:
            myWord = ''.join(sorted(word))
            if myWord in myMap:
                myMap[myWord].append(word)
            else:
                myMap[myWord] = [word]

        return myMap.values()