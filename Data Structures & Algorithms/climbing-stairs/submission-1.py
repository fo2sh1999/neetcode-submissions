class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n 
        x =1  
        y =2 
        remaining = n-2 
        while remaining > 0:
            temp = y
            y = x +y
            x = temp
            remaining -=1
        return y

            