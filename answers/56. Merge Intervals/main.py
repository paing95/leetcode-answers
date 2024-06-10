"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

We are given an array of intervals.
Each interval is an array of start and end.

e.g. [[1,3],[8,10],[15,18],[2,6]]

We are to merge all overlapping intervals and return non-overlapping intervals.

First we should sort the intervals. That way it will be easier to check the overlapping with previous interval.

e.g. [[1,3],[2,6],[8,10],[15,18]]

Then, We should cater an output variable as an array to return as result.
And since first interval does not need any checking, we can add to output.

e.g. [[1,3]]

Loop from second interval check if start element of current interval is less than equal to
last ouput end element.

if it fulfills the condition, we should replace previous interval with
[first element of last output interval, maximum of end of last output element 
and end of current interval element].

if it doesn't fulfill the condition, we can just add current interval to the output.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by first element of intervals
        intervals.sort(key=lambda i: i[0])
        # first interval no need checking
        output = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_element = output[-1]

            if current_interval[0] <= last_element[1]:
                output[-1] = [output[-1][0], max(output[-1][1], current_interval[1])]
            else:
                output.append(current_interval)
        
        return output