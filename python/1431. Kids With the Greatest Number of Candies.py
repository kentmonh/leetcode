"""
Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies 
among the kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        true_false = []
        for candy in candies:
            bol = True if candy >= max(candies) - extraCandies else False
            true_false.append(bol)
        return true_false