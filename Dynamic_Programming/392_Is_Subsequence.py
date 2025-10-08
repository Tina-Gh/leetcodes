# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).




class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ####### O(n^2)
        counter = 0
        flag = 0
        for i in range(len(s)): 
            for j in range(counter, len(t)): 
                if s[i] == t[j]:
                    counter = j+1
                    flag += 1
                    break
        if flag == len(s): # meaning if all the characters were found 
            return True 
        else: 
            return False


        ####### O(n), using the same approach as above, but making it more efficient with a 'while' loop instead of a 'for' loop
        # sp = tp = 0
        # while sp < len(s) and tp < len(t): #sp (aka. s pointer) is the same as i, and tp (aka. t pointer) is the same as j
        #     if s[sp] == t[tp]: 
        #         sp += 1 
        #     tp += 1 
        # return sp == len(s)
                 
                