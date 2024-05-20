"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

Given 9 x 9 sudoku board.
Three conditions to be fulfilled to be a valid sudoku:
1. Each row must contain 1-9 without repetition.
2. Each column must contain 1-9 without repetition.
3. Each of 3 x 3 boxes must contain 1-9 without repetition.

There are non integer values such as ".".
Those can be skipped.

We should have a hashmap and set to keep track of numbers.
e.g. rows = {} and each row index will have set() rows[0] = set()
Then we loop row. on each row, we loop each col.
for 3 x 3 boxes, it we divide by 3 and floor it. we could get the box number.
e.g. row = 0, col 4, row // 3 and col // 3 => box (0, 1)
        
Note that we should not get bigger no of row // 3 and col // 3 and 
we should use tuple for box key instead.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = {}, {}, {}
        
        for r in range(len(board)): # row array
            for c in range(len(board[r])): # element of row array
                if board[r][c] == '.': continue # if value is non integer
                # calculate the box no
                box_no = (r // 3, c // 3)
                # set() if key not in dict
                if r not in rows: rows[r] = set()
                if c not in cols: cols[c] = set()
                if box_no not in boxes: boxes[box_no] = set()

                if board[r][c] in rows[r] or \
                board[r][c] in cols[c] or \
                board[r][c] in boxes[box_no]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[box_no].add(board[r][c])
        
        return True