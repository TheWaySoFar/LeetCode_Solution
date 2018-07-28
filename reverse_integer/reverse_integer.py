#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = list(str(x))

        sign = 1 if s[0] == '-' else 0
        if sign == 1:
            s = s[1:]
        s.reverse()
        ans = ''
        if sign == 1:
            ans = '-'
        for i in s:
            ans = ans + i

        ans = int(ans)
        if ans < -(1<<31) or ans > (1<<31)-1:
            return 0
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(1534236469))