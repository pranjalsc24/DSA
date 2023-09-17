# Add Binary
#     
#    1 1
#      1  1
#    +
#      1  1
#   ------------
#    1 1  0
# 

#    ------another solution-----

#  # ord is use to get value of ASCII character


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        res=''
        carry= 0

        a,b=a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            first= ord(a[i]) - ord("0") if  i< len(a) else 0
            second=ord(b[i]) - ord("0") if  i< len(b) else 0

            total= first+ second+ carry
            char=str(total%2)
            res=char+res
            carry= total//2

        if carry:
            res="1" + res
        return res        


    

        # -- using inbuild libraries--

        # sum=bin(int(a,2)+ int(b,2))
        # return sum[2:]



   
        