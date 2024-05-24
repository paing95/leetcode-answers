"""
48. Rotate Image
https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

Given n x n matrix.
And we need to move the elements clockwise 90 deg.
Without using extra 2D matrix.

    L       R
    1   2   3   T
    4   5   6
    7   8   9   B

First we put [top][left] to a variable.
Move [bottom][left] to [top][left].
Move [bottom][right] to [bottom][left].
Move [top][right] to [bottom][right].
Finally put the [top][left] variable to [top][right].
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left): # only rotate length - 1
                top, bottom = left, right
                # put top left to a variable
                top_left = matrix[top][left+i]

                # put bottom left to top left
                matrix[top][left+i] = matrix[bottom-i][left]

                # put bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]

                # put top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                # finally put top left variable to top right
                matrix[top+i][right] = top_left

            right -= 1
            left += 1

        