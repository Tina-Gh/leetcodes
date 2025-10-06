class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ###### MEMOIZATION 
        memo_lst = [None] * (n+1)
        if n == 0 or n == 1: 
            return 1
        if memo_lst[n] is not None: 
            return memo_lst[n]

        memo_lst[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        return memo_lst[n]

        ###### BOTTOM-UP APPROACH 
        memo_lst = [1, 1]
        for i in range(2, n+1):
            next_one = memo_lst[i-1] + memo_lst[i-2] 
            memo_lst.append(next_one)
        return memo_lst[n]

        ####### SPACE EFFICINET
        curr = 1
        prev = 1
        for i in range(2, n+1):
            temp = curr
            curr += prev 
            prev = temp

        return curr
