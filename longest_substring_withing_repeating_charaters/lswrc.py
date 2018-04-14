class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        d = {}
        l = 0
        ans = 0
        for i, c in enumerate(s):
            if d.setdefault(c, -1) != -1 and d[c] >= l:
                ans = max(ans, i-d[c])
                l = d[c] + 1;
            else:
                ans = max(ans, i - l + 1)

            d[c] = i
        ans = max(ans, len(s) - l)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("c"))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("cdd"))
