# Q2. Maximum Product of Three Elements After One Replacement
# Solved
# Medium
# 4 pt.
# You are given an integer array nums.

# You must replace exactly one element in the array with any integer value in the range [-10^5, 10^5] (inclusive).

# After performing this single replacement, determine the maximum possible product of any three elements at distinct indices from the modified array.

# Return an integer denoting the maximum product achievable.

#  

# Example 1:

# Input: nums = [-5,7,0]

# Output: 3500000

# Explanation:

# Replacing 0 with -105 gives the array [-5, 7, -105], which has a product (-5) * 7 * (-105) = 3500000. The maximum product is 3500000.

# Example 2:

# Input: nums = [-4,-2,-1,-3]

# Output: 1200000

# Explanation:

# Two ways to achieve the maximum product include:

# [-4, -2, -3] → replace -2 with 105 → product = (-4) * 105 * (-3) = 1200000.
# [-4, -1, -3] → replace -1 with 105 → product = (-4) * 105 * (-3) = 1200000.
# The maximum product is 1200000.
# Example 3:

# Input: nums = [0,10,0]

# Output: 0

# Explanation:

# There is no way to replace an element with another integer and not have a 0 in the array. Hence, the product of all three elements will always be 0, and the maximum product is 0.

#  

# Constraints:

# 3 <= nums.length <= 10^5
# -105 <= nums[i] <= 10^55

##########################################################################

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive_nums = []
        for i in nums: 
            if i < 0:
                positive_nums.append(-i)
            else: 
                positive_nums.append(i) 
    
        first_max_num = 0
        second_max_num = 0
        for i in positive_nums:
            if i > first_max_num:
                second_max_num = first_max_num
                first_max_num = i 
            elif i > second_max_num:
                second_max_num = i

        return first_max_num * second_max_num * 100000