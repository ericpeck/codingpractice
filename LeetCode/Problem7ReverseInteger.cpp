/*
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
*/
class Solution {
public:
    int reverse(int x) {
    double reverseNum = 0;
    double leftover;
        while(x != 0){
            leftover = x%10;
            reverseNum = reverseNum*10 + leftover;
            x /= 10;
        }
        if(reverseNum <= -2147483648){
            return 0;
        }
        if(reverseNum >= 2147483647){
            return 0;
        }
        else{
            return reverseNum;
        }     
    }
};