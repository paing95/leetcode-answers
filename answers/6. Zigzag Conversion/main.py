"""
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

We are given a string "PAYPALISHIRING".
And we have to zigzag the char in the string.
P   A   H   N
A P L S I I G
Y   I   R
numsRow => 3

Then, we have to return "PAHNAPLSIIGYIR".

2d array? tmpArr = []
for i in range(numRows): numRows.append([])
row = 0, add = True
while i < len(s):
    col = 0 if len(tmpArr[row]) == 0 else len(tmpArr[row]) - 1
    tmpArr[row][col] = s[i]

    if row + 1 == numRows:
        add = False
    elif row - 1 == -1:
        add = True

    if add:
        row += 1
    else:
        row -= 1
    
    i += 1
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        tmpArr = []
        # create 2d array
        for i in range(numRows): tmpArr.append([])
        row = 0
        add = True
        i = 0
        while i < len(s):
            # just append instead of len - 1
            tmpArr[row].append(s[i])

            # e.g. numsRows = 3, current row is 2
            if row + 1 == numRows:
                add = False
            # e.g. numsRows = 3, current row is 0
            elif row - 1 == -1:
                add = True

            if add:
                row += 1
            else:
                row -= 1
            
            # this needs to keep moving
            i += 1
        
        output = ""
        # join each 2d array into a string
        for i in range(len(tmpArr)): output += "".join(tmpArr[i])
        return output