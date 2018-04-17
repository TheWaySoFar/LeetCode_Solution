#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        l, r, half_len = 0, m, (m+n+1)//2
        while l<=r:
            i = (l + r) // 2
            j = half_len - i
            if i > 0 and nums1[i-1] > nums2[j]:
                r = i - 1
            elif i < m  and j > 0 and nums1[i] < nums2[j-1]:
                l = i + 1
            else:
                if i == 0:
                    lmax = nums2[j-1]
                elif j == 0:
                    lmax = nums1[i-1]
                else:
                    lmax = max(nums1[i-1], nums2[j-1])
                if (m+n) % 2 == 1:
                    return lmax

                if i == m:
                    rmin = nums2[j]
                elif j == n:
                    rmin = nums1[i]
                else:
                    rmin = min(nums1[i], nums2[j])
                return (lmax + rmin) / 2.0

class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for x in nums2:
            nums1.append(x)
        nums1.sort()
        l = len(nums1)
        if l % 2 == 1:
            return nums1[l//2]
        else:
            return (nums1[l//2]+nums1[(l-1)//2])/2
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))