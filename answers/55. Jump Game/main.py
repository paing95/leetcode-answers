"""
55. Jump Game
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer array "nums" and consider we are at first index of the array.
The value at "i" position represents the max jump "i" position can do.
We will need to return "true" if jumping can reach last index or return "false".

e.g. nums = [2,3,1,1,4], Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

It will be difficult to start from index 0 cos we will have to consider all possible moves.
Also the main point is whether can reach last index or not. 
Which also means if the last index can reach first index or not.
Let's start from the back and we try shifting the pointer and see if can reach that pointer.
e.g. if index 3 (1) can reach index 4 (4), move pointer to index 3 (1).
then we check if index 2 (1) can reach index 3 (1), move pointer to index 2 (1). and so on.


Let's have a variable called "goal".
On a for loop starting from len(nums) - 2:
    we check if i element can reach goal,
        if so, we shift the goal to i
Outside the loop, we check if goal == 0 then return true else false
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0: return True
        return False