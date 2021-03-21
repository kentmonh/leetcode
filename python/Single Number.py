"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
class Solution:
    # Bit Manipulation (Use XOR)
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for number in nums:
            ans = ans ^ number
        return ans