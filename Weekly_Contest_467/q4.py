# Q4. Number of Stable Subsequences
# Hard, 6 points

# You are given an integer array nums.

# A subsequence is stable if it does not contain three consecutive elements with the same parity when the subsequence is read in order (i.e., consecutive inside the subsequence).

# Return the number of stable subsequences.

# Since the answer may be too large, return it modulo 10 ** 9 + 7.

#

# Example 1:

# Input: nums = [1,3,5]

# Output: 6

# Explanation:

# Stable subsequences are [1], [3], [5], [1, 3], [1, 5], and [3, 5].
# Subsequence [1, 3, 5] is not stable because it contains three consecutive odd numbers. Thus, the answer is 6.

#

# Example 2:

# Input: nums = [2,3,4,2]

# Output: 14

# Explanation:

# The only subsequence that is not stable is [2, 4, 2], which contains three consecutive even numbers.
# All other subsequences are stable. Thus, the answer is 14.

#

# Constraints:

# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
################################## Tina.G ##################################

# Technique 1, without dynamic programming 
# cons: Time Limit Exceeded on Leetcode (aka. 2^n subsequences for a sequence of n which is exponential and big!)

class Solution(object):
    def countStableSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        subseq_lst = [[]]
        for item in nums:  
            # new_subsequences = [sub + [item] for sub in subsequences]
            new_subseq_lst = []
            for sub in subseq_lst: 
                if self.check_parity((sub+[item])): 
                    new_subseq_lst.append(sub + [item])
                else: 
                    continue 
            subseq_lst.extend(new_subseq_lst)

        return (len(subseq_lst) - 1)% MOD # - 1 becase of the null subsequence []
        # print(subseq_lst)


    def check_parity(self, lst): 
        if len(lst) >= 3:
            i = 0
            while i+2 < len(lst): 
                if (lst[i]%2 == 0) and (lst[i+1]%2 == 0) and (lst[i+2]%2 == 0): #is even 
                    return False
                elif (lst[i]%2 == 1) and (lst[i+1]%2 == 1) and (lst[i+2]%2 == 1): #is odd
                    return False  
                i += 1
            return True
        else: 
            return True 

################################## Tina.G ##################################
# Technique 2, using dynamic programming 

class Solution(object):
    def countStableSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        dp_even = [0, 0, 0] # we don't need index 0. need only 1, & 2. 0 so it's more intuitive
        dp_odd = [0, 0, 0] 

        for x in nums: 
            px = x % 2 # parity of x
            new_dp_even = dp_even[:]
            new_dp_odd = dp_odd[:] 

            if px == 0: # even 
                # start new subsequence with x
                new_dp_even[1] = (new_dp_even[1] + 1) % MOD

                # extend subsequences
                new_dp_even[1] = (new_dp_even[1] + dp_odd[1] + dp_odd[2]) % MOD # switch parity
                new_dp_even[2] = (new_dp_even[2] + dp_even[1]) % MOD # extend streak
                
            else: # odd
                new_dp_odd[1] = (new_dp_odd[1] + 1) % MOD 
                new_dp_odd[1] = (new_dp_odd[1] + dp_even[1] + dp_even[2]) % MOD
                new_dp_odd[2] = (new_dp_odd[2] + dp_odd[1]) % MOD

            dp_even = new_dp_even[:] # updating 
            dp_odd = new_dp_odd[:]

        return (sum(dp_even) + sum(dp_odd)) % MOD
                






