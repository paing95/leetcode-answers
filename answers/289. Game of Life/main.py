"""
289. Game of Life
https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

Given a matrix m x n.
Possible values are 0 and 1.
1 represents "live" and 0 represents "dead".
We are to check the eight neighbour cells and change the cell value in following conditions.
        
1. Change 1 to 0 if neighbours with 1 are less than two.
2. Change 1 to 0 if neighbours with 1 are more than three.
3. Change 0 to 1 if neighbours with 1 are three.

If we are to replace the values in-place, we have to change the values to sth else when we change.
Example is as below.

    Overview of states

    Old     New     Value
    0       0       0
    1       0       1
    0       1       2
    1       1       3

"""
class Solution:

    def getLiveNeighbours(self, row, col, board):
        count = 0
        # start from top left row and col
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                # ignore cases
                # 1. if current r,c pair is the same as row, col pair
                # 2. if out of bound
                if (r == row and c == col) or r < 0 or c < 0 or c >= len(board[0]) or r >= len(board) :
                    continue
                # 3 have to be checked because of our mapping
                if board[r][c] == 1 or board[r][c] == 3: count += 1
        
        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        row_length = len(board)
        col_length = len(board[0])
        
        for row in range(row_length):
            for col in range(col_length):
                live_neighbours = self.getLiveNeighbours(row, col, board)
                
                if board[row][col] == 1:
                    if live_neighbours >= 2 and live_neighbours <= 3:
                        board[row][col] = 3
                elif board[row][col] == 0 and live_neighbours == 3:
                    board[row][col] = 2
        
        for row in range(row_length):
            for col in range(col_length):
                if board[row][col] == 3 or board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == 1 or board[row][col] == 0:
                    board[row][col] = 0