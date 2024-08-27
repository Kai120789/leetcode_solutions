class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 0
        max_price = 0

        res = 0

        """ if len(prices) >= 10**5:
            return res """

        count = 0
        count2 = 1
        while count2 < len(prices):

            if prices[count2] > prices[count]:
                min_price = prices[count]
                max_price = prices[count2]

            if max_price - min_price > res:
                res = max_price - min_price

            
            if prices[count] > prices[count2]:
                count = count2
                count2 = count + 1
            else:
                count2 += 1
        
        return res