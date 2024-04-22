"""
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

Given an array called "prices" and prices[i] is price of a stock on "i" day.
Can hold only one stock at a time. Meaning after buying a stock, cannot buy another time.
Can buy and sell the stock at the same day. But what's the point cos there is no profit.
We have to return the max profit we can achieve.

prices = [7,1,5,3,6,4], Output is 7, 
buy on day 2 (1) and sell on day 3 (5) => profit is 4,
buy on day 4 (3) and seel on day 5 (6) => profit is 3,
combine those two => total profit is 7. 

 |  7   *
 P  6                   *
 R  5           *
 I  4                       *
 C  3               *
 E  2
 |  1       *
    0   1   2   3   4   5   6
            --- DAY ----

So how do we calculate this? 
Base rule is we buy and sell when price[i] is greater than price[n] as we knew already on question 121.
However, we may need to sell more than one time here. 
If we refer back to the example, notice that we buy at i day and selling at the next day that has greater price.
let's write a logic based on this for O(n).

we will have l, r pointers and profit to keep track.
We do a while loop till r <= len(prices) - 1
    if prices[r] > prices[l]:
        profit += prices[r] - prices[l]
    l = r
    r += 1
""" 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit = 0, 0, 0
        while r <= len(prices) - 1:
            if prices[r] > prices[l]:
                profit += prices[r] - prices[l]
            l = r
            r += 1
        return profit