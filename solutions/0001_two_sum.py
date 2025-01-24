"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Store the previous values in a hash and check if the target difference is already in the hash if not
        insert the current number: index into the hash
        """
        results = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in results:
                return [i, results[diff]]
            results[num] = i


class Test:
    def test(self):
        case = [[2, 7, 11, 15], 9]
        expected = [0, 1]

        assert sorted(Solution().twoSum(*case)) == expected
