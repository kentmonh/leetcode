class Solution:
    def arrangeCoins(self, n: int) -> int:
        numberOfRows = 1
        numberOfCoins = 1 
        if n == 0:
            return 0
        else:
            while numberOfCoins <= n:
                numberOfRows += 1
                numberOfCoins += numberOfRows
            return (numberOfRows - 1)