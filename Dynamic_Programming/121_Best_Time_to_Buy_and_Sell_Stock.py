# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ####### O(n^2), takes too long!
        # max_profit = 0
        # for i in range(len(prices)): 
        #     for j in range(i+1, len(prices)):
        #         temp = prices[j] - prices[i]
        #         if max_profit < temp: 
        #             max_profit = temp
        # return max_profit


        ####### O(n), we don't need to keep a nice track of 'buy', it can get updated but the 'profit' is what we keep.
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)): 
            if prices[i] < buy:
                buy = prices[i] 
            elif prices[i] - buy > profit: 
                profit = prices[i] - buy
        return profit 
        