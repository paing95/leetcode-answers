"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

Given an array called "prices" and prices[i] is price of a stock on "i" day.
We have to find the max possible profit by buying the stock the "i" day and "i + n" day.
And return the max profit. If cannot sell, return 0.

prices = [7,1,5,3,6,4], Output is 5, buy on day 2 (1) and sell on day 5 (6), 6 - 1 = 5

 |  7   *
 P  6                   *
 R  5           *
 I  4                       *
 C  3               *
 E  2
 |  1       *
    0   1   2   3   4   5   6
            --- DAY ----
If we draw on graph, the stock price will look like this.

Obviously day 1 to 2, we are not selling cos stock goes down.
Then we move to day 2 to 3, we can buy at day 2 and sell at day 3. profit is 4.
But it is not the most profit you can get. We knew that we have to buy at day 2 and sell at day 5.
At this situation, we should not move the buying day. Instead we should move the selling day.
But at some other examples, there will be conditions that we have to move the buying day.
So what are the conditions? The condition is to move buying day only if selling day is smaller.

Let's have a loop that runs O(n) time with l and r pointers and a variable called "profit".
We shall run until r <= len(prices) - 1. That's while loop.
Inside the while loop,
    profit = max(profit, prices[r] - prices[l])
    if prices[r] < prices[l]: then we should do l = r
    then we do r += 1

* Remember to move the l to r when r price is lower than l price instead of simply doing l += 1.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit = 0, 0, 0
        while r <= len(prices) - 1:
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]: l = r
            r += 1
        return profit