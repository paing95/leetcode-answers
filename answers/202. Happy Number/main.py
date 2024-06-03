"""
202. Happy Number
https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150

We are to check if number "n" is happy.
"happy" number can be defined when
1. Starts with positive integer.
2. Replace the number by the sum of the squares of its digit.
3. Repeat no.2 until number equals 1 or runs out.

First of all, we need to split the number to individual integer.
So how? We should start with a 10.
modulus by 10 - if has value from that - value x value and save it to a variable "res"
again modulus by 10 - if has value from that - value x value and save it to a variable
no more value from divide by 10 - stop

Trick here is to know if that variable "res" falls below 10, we should stop.
However, we have to return true if "res" is either 1 or 7.

OR

We could use a hashmap to keep track of all possible numbers.
And stop if "res" is 1.
"""
class Solution:
    def countTheNums(self, num: int) -> int:
        number = num
        res = 0
        while number:
            tmp = number % 10
            res += tmp ** 2
            number = number // 10
        return res

    def isHappy(self, n: int) -> bool:
        # without using a map
        """
        number = n
        res = 0
        while True:
            res = self.countTheNums(number)
            number = res
            if res < 10: break
        
        return True if res in [1, 7] else False
        """
        myMap = {}
        number = n
        while number not in myMap:
            myMap[number] = 1
            number = self.countTheNums(number)
            if number == 1: return True
        return False