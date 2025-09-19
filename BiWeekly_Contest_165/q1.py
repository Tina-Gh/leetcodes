# Q1: smallest absent positive greater than average: 
# Easy,  3 points

# You are given an integer array nums.

# Return the smallest absent positive integer in nums such that it is strictly greater than the average of all elements in nums.

# The average of an array is defined as the sum of all its elements divided by the number of elements.

#  

# Example 1:

# Input: nums = [3,5]

# Output: 6

# Explanation:

# The average of nums is (3 + 5) / 2 = 8 / 2 = 4.
# The smallest absent positive integer greater than 4 is 6.

#

# # Example 2:

# Input: nums = [-1,1,2]

# Output: 3

# Explanation:

# ​​​​​​​The average of nums is (-1 + 1 + 2) / 3 = 2 / 3 = 0.667.
# The smallest absent positive integer greater than 0.667 is 3.

#

# Example 3:

# Input: nums = [4,-1]

# Output: 2

# Explanation:

# The average of nums is (4 + (-1)) / 2 = 3 / 2 = 1.50.
# The smallest absent positive integer greater than 1.50 is 2.

#  

# Constraints:

# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100​​​​​​​©leetcode
################################## Tina.G ##################################

class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        if max(nums) < 0: 
            output = 1 
            return output
                    
        mean = sum(nums)/len(nums)
        if mean <= 0: 
            initial = 1
        else: # works whether if mean is int or has decimal number
            initial = int(mean) + 1 
    
        for i in range(initial, max(nums)+1): 
            if i not in nums: 
                output = i
                return output
        output = max(nums) + 1        
        return output

        negative_lst = []
        for i in range(len(nums)): 
            if nums[i] <= 0: 
                negative_lst.append(nums[i])
        nums.remove(negative_lst) 

        # # This could be another approach but needs further edits 
        # clipped_nums = list(filter(lambda item: item > 0 and item in nums, nums))
        # if len(clipped_nums) < len(nums): 
        #     clipped_nums.append(0)
        # unique_nums = list(set(clipped_nums))
        # unique_nums.sort()
        # N = len(unique_nums)
        
        # for i in range(N): 
        #     if (unique_nums[i+1] - unique_nums[i] >= 2) and (int(mean) + 1 not in unique_nums): 
        #         if int(mean) > 0:
        #             print(int(mean))
        #             output = int(mean) + 1 # unique_nums[i] + 1
        #             return output 
        #         else: 
        #             print(int(mean))
        #             output = unique_nums[i] + 1
        #             return output 

        # output = unique_nums[-1] + 1
        # return output 
            