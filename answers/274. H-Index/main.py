"""
274. H-Index
https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150


Given an integer array called "citations".
citations[i] is number of citations i paper got.
We need to find The h-index that is defined as the maximum value of h such that the given researcher 
has published at least h papers that have each been cited at least h times.

e,g, citations = [3,0,6,1,5], Output is 3.
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total 
and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and 
the remaining two with no more than 3 citations each, their h-index is 3.

How to solve this?
Intial step is to sort the array in reverse.
e.g. [3,0,6,1,5] => [6, 5, 3, 1, 0]
Then, we create a variable to store h_index and we do a for loop.
    Inside the loop,
        we check if h_index >= citations[i]: break
        h_index += 1
    Finally, returh h_index
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if h_index >= citations[i]: break
            h_index += 1
        return h_index