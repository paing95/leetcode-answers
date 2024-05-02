"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

first we should keep the dictionary of all possible symbols.

symbol_dict = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

And we should keep the dictionary for special symbols that could have special conditions.

with_special_symbols = {
    'I': 1,
    'X': 1,
    'C': 1
}

first we loop the string from the back.
value = 0
i = len(s) - 1
while i >= 0:
    if i > 0 and s[i-1] in with_special_symbols and "{0}{1}".format(s[i-1], s[i]) in symbol_dict:
        value += symbol_dict["{0}{1}".format(s[i-1], s[i])]
        i -= 2
    else:
        value += symbol_dict.get(s[i], 0)
        i -= 1
return the value;

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        with_special_symbols = {
            'I': 1,
            'X': 1,
            'C': 1
        }
        value = 0
        i = len(s) - 1
        while i >= 0:
            if i > 0 and s[i-1] in with_special_symbols and "{0}{1}".format(s[i-1], s[i]) in symbol_dict:
                value += symbol_dict["{0}{1}".format(s[i-1], s[i])]
                i -= 2
            else:
                value += symbol_dict.get(s[i], 0)
                i -= 1
        return value
