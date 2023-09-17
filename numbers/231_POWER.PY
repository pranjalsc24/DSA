# POWER OF TWO
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # ---------below solution is right but memory is exceeding----------
        # s=n//2
        # if n==1:
        #     return True
        # if n%2!=0:
        #     return False    
        # for i in range(0,s+1):
        #     if 2**i==n:
        #         return True
        # return False    
            
           
               

        while n:
            if n == 1:
                return True
            elif n % 2 == 0:
                n /= 2
            else:
                return False
        