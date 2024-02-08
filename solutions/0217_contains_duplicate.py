#!/usr/bin/env python3

"""
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct.
"""

from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Create a hash with the prev values the search is O(1)
        with this the final complexity is O(n)
        """
        prev_values = {}
        for num in nums:
            if num in prev_values:
                return True
            prev_values[num] = num
        return False


class Test:
    def test(self):
        """[Test description.]"""
        case = [1,1,1,3,3,4,3,2,4,2]
        expected = True

        assert Solution().containsDuplicate(case) == expected

    def test_fail(self):
        pass
