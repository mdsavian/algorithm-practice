"""
LeetCode 217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/

"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)

        return len(newSet) != len(nums)
