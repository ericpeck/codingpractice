'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x > 2147483647 or x < -2147483648):
            return 0
        if(x >= 0):
            hello = [int(i) for i in str(x)]
            hello.reverse()
            r = int("".join(map(str,hello)))
            if(r > 2147483647):
                return 0
            else:
                return r
        if(x < 0):
            x *= -1
            hello = [int(i) for i in str(x)]
            hello.reverse()
            r = int("".join(map(str,hello)))
            r *= -1
            if(r < -2147483648):
                return 0
            else:
                return r