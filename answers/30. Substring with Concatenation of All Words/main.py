"""
30. Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150

Given a string called "s" and an array of strings called "words".
Each string in "words" array has the same length.

A concatenated string is a string that exactly contains 
all the strings of any permutation of "words" concatenated.

We are to find the starting indices of all the concatenated substrings (from words array) in s. 
You can return the answer in any order.

The logic to solve this problem.
Start from left, starts a loop.
    On each loop,
        We have to do another loop and on each loop, we have to examine the string from the index.
        until index + total length of all members of "words" array.
        
            Inside the loop, we have to memorise if all members from the "words" array exist in the cut string.
            using a map.
        
        outside the loop, we check the memorised value.
            if all members from "words" array in the cut string, store the index in an array.
        After that, plus one to the index.
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        res = []
        total_words = len(words)
        each_word_length = len(words[0])
        s_length = len(s)
        possile_max_length = total_words * each_word_length

        main_mapping = {}
        for word in words:
            if word not in main_mapping: main_mapping[word] = 0
            main_mapping[word] += 1

        l = 0
        while l in range(s_length):
            copied_mapping = main_mapping.copy()
            end = possile_max_length + l 
            myCount = total_words
            main_valid = False
            for i in range(l, end, each_word_length):
                if i >= s_length: break
                
                if i > l and not main_valid: break

                is_valid = True
                myStr = s[i : i + each_word_length]
                if myStr in copied_mapping:
                    copied_mapping[myStr] -= 1
                else:
                    is_valid = False
                
                if copied_mapping.get(myStr, -1) < 0:
                    is_valid = False
                
                main_valid = is_valid
                if main_valid: myCount -= 1
            
            if main_valid and myCount == 0:
                res.append(l)
            l += 1
        return res
