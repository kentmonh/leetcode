import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set initial buy, sell price and profit
        buy = prices[0] # math.inf
        sell = 0 # -math.inf
        isBought = False
        profit = 0
        # buy if price in bottom (prices[i-1] > prices[i] < prices[i+1])
        # sell if price in top (prices[i-1] < prices[i] > prices[i+1])
        for i in range(1, len(prices)):
            if isBought == False:
                if prices[i] <= buy:
                    buy = prices[i]
                else:
                    sell = prices[i]
                    isBought = True
                    if i == (len(prices) - 1):
                        profit += (sell - buy)
            else:
                if prices[i] >= sell:
                    sell = prices[i]
                    if i == (len(prices) - 1):
                        profit += (sell - buy)
                else:
                    profit += (sell - buy)
                    isBought = False
                    sell = 0
                    buy = prices[i]
        return profit 