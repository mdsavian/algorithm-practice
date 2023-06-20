"""
LeetCode 1. Two Sum

https://leetcode.com/problems/two-sum/

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i, j]

        hashmap = {}
        for i, n in enumerate(nums):  # O(n)

            diff = target - n

            if (diff in hashmap):
                # O(1) - acessing the position directly
                return [hashmap[diff], i]

            hashmap[n] = i

        return []
