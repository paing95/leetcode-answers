"""
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

We have to change any given int to Roman letters.
Mapping between int and Roman:

I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Special cases:
    IV => 4
    IX => 9
    XL => 40
    XC => 90
    CD => 400
    CM => 900

We will probably have to divide by largest to smallest mapping.
The mapping should include special cases too.

we should write a separate method for division and remainder.
def divide_by(value, divide):
    return value / divide, value % divide

Inside the main function:
    Create a mapping:
        {1000: M, ...}
    Values
        [1000, 900, 500, 400, ...]
    a pointer = 0, a string = ""
    A while loop till num runs out:
        value, remainder = divide_by(num, values[pointer])
        if value:
            string += mapping[value] * value
        num = remainder
    return string
"""
class Solution:

    def __init__(self):
        self.mapping = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        self.dividers = sorted(self.mapping.keys(), reverse=True)

    def divide_by(self, value, divider):
        return value // divider, value % divider
    
    def get_roman_string(self, number):
        return self.mapping.get(number, "")

    def intToRoman(self, num: int) -> str:
        pointer, roman_string = 0, ""
        while num > 0:
            if num < self.dividers[ pointer ]:
                pointer += 1
                continue

            value, remainder = self.divide_by(num, self.dividers[ pointer ])
            if value: 
                roman_string += self.get_roman_string(
                    self.dividers[ pointer ]
                ) * value
            num = remainder
            pointer += 1
        return roman_string