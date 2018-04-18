#!/usr/bin/menv python3
# -*- coding: utf-8 -*-
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        dp = [[0 for i in range(l)] for i in range(l)]

        for i in range(l):
            dp[i][i] = 1
        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
        for i in range(3, l+1):
            for j in range(l - i + 1):
                left, right = j, j+i-1
                if left + 1 <= right -1:
                    dp[left][right] = 1 if dp[left+1][right-1] and s[left]==s[right] else 0
        ansl, ansr, maxl = 0, 0, 1
        for i in range(l):
            for j in range(i, l):
                if dp[i][j] == 1:
                    if j-i+1>maxl:
                        ansl, ansr = i, j
                        maxl = j-i+1
        return s[ansl:ansr+1]

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("ccc"))