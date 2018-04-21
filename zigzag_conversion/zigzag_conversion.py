#!/usr/bin/env python3
# -*- conding: utf-8 -*-

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s);
        if l == 0 or numRows <= 1:
            return s
        row = ["" for i in range(numRows)]
        step = 1
        cnt = 0
        ans = ""
        for i in range(l):
            if cnt == 0:
                step = 1
            if cnt == numRows - 1:
                step = -1
            row[cnt] += s[i]
            cnt += step
        for x in row:
            ans += x
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
    print(s.convert("P", 1))
    print(s.convert("PAYPALISHIRING", 1))
    print(s.convert("", 3))