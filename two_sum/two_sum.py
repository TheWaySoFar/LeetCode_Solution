#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, x in enumerate(nums):
            if target -x in d:
                return d[target - x], i
            d[x] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 5], 9))