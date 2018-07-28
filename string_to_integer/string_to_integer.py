#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        m = re.match(r'^([-+]?[0-9]+).*', str)
        if not m:
            return 0
        num_of_str = m.group(1)
        num = int(num_of_str)
        if num < 0 and num < (-2 ** 31):
            return -2**31
        if num > 0 and num > 2**31 - 1:
            return 2**31 - 1
        return num

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi(""))
    print(s.myAtoi("     -42"))
    print(s.myAtoi("4223 with word"))
    print(s.myAtoi("word with 42"))
    print(s.myAtoi("-912834723320000000"))
    print(s.myAtoi("91283472332"))
