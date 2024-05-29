"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

We are given two strings: s and t.
And check if those two are isomorphic.

We should create a map, a set and loop through s or t.
Since the length of s and t are the same, no need to check the length.
In a loop, we check if current "s" char is in the map.
if not and current "t" is already in the set, return false.
We place map[ current "s" ] = current "t" if not eixst.
if already exists, check if current "s" value in the map is same as current "t".
if not, return false.
Lastly, add to set.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myMap = {}
        mySet = set()
        for x in range(len(s)):
            if s[x] not in myMap and t[x] in mySet:
                return False

            if s[x] not in myMap:
                myMap[ s[x] ] = t[x]
                
            if myMap[ s[x] ] != t[x]: return False
            
            mySet.add(t[x])
        
        return True