"""
135. Candy
https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150

Given an integer array called "ratings". len(ratings) is the number of students.
We are to give the students candies based on ratings.

Two conditions
1. Each student should have one candy.
2. Student with higher rating get more candies than their neighbors.

As a output, we are to return the minmum candies.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Let's look at the example 1:
    Index 0 => 1
        if we look at the neighbours index 1 => 0, rating at index 1 is less than rating at index 0,
        considering the neighbours, 
            per rule 1. index 0 and 1, both should have one candy as a base.
            per rule 2. since index 0 value is bigger than index 1 value, index 0 should be given one more candy.
    Index 1 => 0
        considering the neighbours,
            per rule 1. index 0, 1, and 2 should have at least one candy.
            per rule 2, index 1 value is smaller than index 0 value and index 1 value.
                In case if index 1 value is smaller than index 0 value but bigger than index 1. e.g. [3, 1, 2]
                    Should index 0 be given one more candy? => yes
    Index 2 => 2
        considering the neighbours,
            per rule 1. index 1 and 2 should have at least one candy.
            per rule 2, index 1 value is smaller than index 2 value. so should be given one more candy.

Solution:
let's have an array called candies that has same length as ratings array.
    We can give one candy to every child per rule 1 before we loop for rule 2.
    candies = [1] * len(ratings)
    We could loop and check previous and current and next rating at the same time.
    However, its complication is high.

    Easiest way is to loop two ways.
    loop from 1 to len(ratings) - 1, and check if current rating is higher than previous rating,
        then set current candies = previous candies + 1
    loop from len(ratings) - 2 to 0, and check if current rating is higher than previous rating,
        in this case, instead of simply setting current candies = previous candies + 1
        we will have to check if current candies is already greater than previous candies + 1
        only set current candies to max of those two values
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]: candies[i] = candies[i-1] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]: candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)
