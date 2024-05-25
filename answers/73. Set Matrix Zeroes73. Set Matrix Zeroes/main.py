"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

Given an integer matrix (m x n).
If an element is 0, we will need to set the entire row and column to 0.

The trick is to use two extra arrays.
One for row and one for column.

We should do a nested loop.
Starting from row then to column.
Inside the nested loop, we check if element is 0.
If it's 0, set the value in "rows" extra array to 0.
And set the value in "cols" extra array to 0.

After that, we do two more nested loop.
First to "rows" extra array.
If element is 0, set the whole row to 0.

Lastly to "cols" extra array.
If element is 0, set the whole column to 0.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col_length = len(matrix[0])
        row_length = len(matrix)
        rows = [1] * row_length
        cols = [1] * col_length

        for r in range(row_length):
            for c in range(col_length):
                if matrix[r][c] == 0 and rows[r] != 0:
                    rows[r] = 0
                if matrix[r][c] == 0 and cols[c] != 0:
                    cols[c] = 0
        
        for r in range(row_length):
            if rows[r] == 0:
                for c in range(col_length):
                    matrix[r][c] = 0
        
        for c in range(col_length):
            if cols[c] == 0:
                for r in range(row_length):
                    matrix[r][c] = 0