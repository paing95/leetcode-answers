"""
    54. Spiral Matrix
    https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150
    Given m x n matrix and we have to return all the elements in sprial order.
    To solve this problem, we should have four indexes: left, right, top and bottom.
    left = 0, right = len(matrix[0]) => row pointers
    top = 0, bottom = len(matrix) => col pointers
    [ 1     2      3]
    [ 4     5      6]
    [ 7     8      9]

    first we loop from left to right
    for i in range(left, right): res.append(matrix[top][i])
    and we have to increase top so no duplicate is in results
    top += 1

    then we loop from top to bottom
    for i in range(top, bottom): res.append(matrix[right][i])
    and we have to decrease right so no duplicate is in results
    right -= 1

    for edge cases such as one row/column matrix 
    let's check if len(res) == len(m * n) then break

    After that, we loop from right to left
    for i in range(right-1, left - 1, -1): res.append(matrix[bottom-1][i])
    and we have to decrease bottom so no duplicate in results
    bottom -= 1

    Lastly, we loop from bottom to top
    for i in range(bottom-1, top-1, -1): res.append(matrix[left][i])
    and we have to increase left so no duplicate in results
    left += 1
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLength, colLength = len(matrix), len(matrix[0])
        totalCount = rowLength * colLength
        res = []
        left, right = 0, colLength
        top, bottom = 0, rowLength
        while len(res) < totalCount:
            # left to right
            for i in range(left, right): res.append(matrix[top][i])
            top += 1

            # top to bottom
            for i in range(top, bottom): res.append(matrix[i][right-1])
            right -= 1

            # for single row/column matrixes
            if len(res) == totalCount: break

            # right to left
            for i in range(right-1, left-1, -1): res.append(matrix[bottom-1][i])
            bottom -= 1

            # bottom to top
            for i in range(bottom-1, top-1, -1): res.append(matrix[i][left])
            left += 1
        
        return res

