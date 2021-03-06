"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numberOfPairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    numberOfPairs += 1
        return numberOfPairs
