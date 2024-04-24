"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

We are given an integer array "nums" that has a length of "n".
Each element at index "i" can jump the maximum value of "i" + "j". "j" is nums[i].
We are to return minimum number of jumps that can reach to the end of the array from the start of the array.

e.g. nums = [2,3,1,1,4], Output is 2.
The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Let's analyze the example.
Start from index 0. Value is 2. That means its max jump (i + j) is 2 (0 + 2).
It also means it can jump to index 1 and 2.

Let's look at index 1 and 2. 
Index 1 has value 3. It means its max jump is 4 (1 + 3). At this point we have reached to the end.
Index 2 has value 1. It means its max jump is 3 (2 + 1).


How to solve.
Let's have three variables: l, r, j and set their values to 0.
Then we do a while loop until r < len(nums) - 1
    inside the loop,
        maxi = 0
        we do another while loop (l <= r)
            we do maxi = max(maxi, nums[l] + l)
            and l += 1
        l = r + 1
        r = maxi
        j += 1

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, j = 0, 0, 0
        while r < len(nums) - 1:
            maxi = 0
            while l <= r:
                maxi = max(maxi, nums[l] + l)
                l += 1
            l = r + 1
            r = maxi
            j += 1
        return j