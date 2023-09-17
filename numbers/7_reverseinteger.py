# The abs() function in Python returns the absolute value of a number, which is the magnitude of the number without considering its sign. If x is a positive number or zero, abs(x) will be equal to x itself. If x is a negative number, abs(x) will be equal to the positive value of x.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        r=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x:
            d=x%10
            r=r*10+d
            x/=10
        result=sign*r 

        if result>2**31-1 or result< -(2**31):
            return 0   
        return result    




