# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Follow up:
# 1. It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# 2. Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?



class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ####### O(nlogn) APPROACH 
        # lst_ones = []
        # for i in range(0, n+1): 
        #     counter = 0
        #     while i > 0: 
        #         remainder = i % 2
        #         if remainder == 1: 
        #             counter += 1
        #         i //= 2 
        #     lst_ones.append(counter)
        # return lst_ones
        
        
        ####### same time complexity as above but with buil-in function 
        # lst_ones = []
        # for i in range(0, n+1): 
        #     lst_ones.append(bin(i).count('1'))

        # return lst_ones


        ####### O(n) APPROACH (with dictionary or list) 
        # dict_ones = {}
        # dict_ones[0] = 0

        # for i in range(0, n+1): 
        #     dict_ones[i] = dict_ones[i//2] + i%2

        # return list(dict_ones.values())

        lst_ones = [None]*(n+1)
        lst_ones[0] = 0 

        for i in range(0, n+1): 
            lst_ones[i] = lst_ones[i//2] + i%2 # or: if i is even, then append lst_ones[i//2]; otherwise append lst_ones[i//2] + 1

        return lst_ones
    




        