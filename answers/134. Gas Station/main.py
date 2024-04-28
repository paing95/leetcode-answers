"""
134. Gas Station
https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

Given an integer arrays called "gas" and "cost".
gas[i] is the gas available at index i.
cost[i] is the gas requied to travel to index i+1 station.

We are to return he starting gas station's index 
if you can travel around the circuit once in the clockwise direction, otherwise return -1. 

Solution wil be unique.

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

[  1,  2,  3, 4, 5 ] => gas
[  3,  4,  5, 1, 2 ] => cost
[ -2, -2, -2, 3, 3 ] => diff
3 => answer

if we sum the diff array, we get the 0 as result.
At this point, we should check if total of all gas < total of all cost, there's no start point.

After that check, we keep variables called "fuel" and "position".
let's say we iterate through the array.
    on each iteration, we check gas[i] - cost[i] is below 0
    it means it cannot travel to next station and so it cannot be start point.    
    if cannot be the start point, let's put next (i+1) as start point temporarily.
    at this point, we need to reset fuel as it is a start point.
    
    does it matter if fuel is reset and does not count for previous values?
    no. Because we already checked if total of all gas < total of all cost.
    And we knew for a fact that a solution has to exist.
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        fuel, position = 0, 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                position = i + 1
                fuel = 0
        return position
