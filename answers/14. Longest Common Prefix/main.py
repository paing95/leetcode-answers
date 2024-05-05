"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Let's assign first item to output.

From second item and onwards, we just 
1. compare output and current item
2. remove the chars that differ from the output.

Edge cases 
1. when output length is greater than current item.
2. when output and current item are not the same at index 0.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        for i in range(1, len(strs)):
            x = 0
            while x < len(strs[i]):
                if x < len(output) and output[x] != strs[i][x]:
                    if x > 0: 
                        output = output[:x]
                    else:
                        output = ""
                    break
                x += 1
            if len(output) > len(strs[i]): output = output[:len(strs[i])]
        return output