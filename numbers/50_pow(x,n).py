# https://www.youtube.com/watch?v=g9YQyYi4IQQ&ab_channel=NeetCode

# 2^10=2^5 * 2^5
# 2^5= 2^2 * 2^2 * 2   ----for odd numbers
# 2^2= 2 * 2





class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
# -----------using inbuild--------
        # ans=x**n
        # return ans


# ------------normal way--------
        def helper(x,n):
            if x==0: return 0
            if n==0: return 1

            res=helper(x,n//2)
            res=res*res
            return x*res if n%2 else res

        res =helper(x,abs(n))
        return res if n>=0 else 1/res   




        