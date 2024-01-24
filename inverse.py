'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
'''


class Solution:
    def reverse(self, x: int) -> int:
        isneg = False
        if x < 0:
            isneg = True
        else:
            isneg = False #redundant
            
        product = abs(x)
        remainder = 0
        iter = 0
        result = 0
        
        while product != 0:
            remainder = product % 10 #2
            product = product // 10  # 1
            result = (result * 10 + remainder) # 3* 10 + 2 = 32
            iter += 1
            

            
        
        if isneg:
            result = result * (-1) 
            
        return result
    
if __name__ == "__main__":
    answer = Solution()
    print(answer.reverse(-123))