# Q1. Earliest Time to Finish One Task 
# Easy, 3 points

# You are given a 2D integer array tasks where tasks[i] = [si, ti].

# Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.

# Return the earliest time at which at least one task is finished.

#

# Example 1:

# Input: tasks = [[1,6],[2,3]]

# Output: 5

# Explanation:

# The first task starts at time t = 1 and finishes at time 1 + 6 = 7. The second task finishes at time 2 + 3 = 5. You can finish one task at time 5.

#

# Example 2:

# Input: tasks = [[100,100],[100,100],[100,100]]

# Output: 200

# Explanation:

# All three tasks finish at time 100 + 100 = 200.

#

# Constraints:

# 1 <= tasks.length <= 100
# tasks[i] = [si, ti]
# 1 <= si, ti <= 100

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
################################## Tina.G ##################################


class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        finish_time = []
        for t in tasks: # ([t[0]+t[1]] for t in tasks0
            # if t[0] >= 1 and t[1]>=100: # while
            finish_time.append(t[0]+t[1]) 
                
        return min(finish_time)

        

