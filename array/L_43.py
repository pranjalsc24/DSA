# Multiply Strings
# Input: num1 = "123", num2 = "456"
# Output: "56088"

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #---------- inbuild-----------
        # n=int(num1)
        # m=int(num2)
        # return str(n*m)

        
        
        dict1 = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        val1=0
        val2=0
        for i in num1:
            ans1 = dict1[i]
            val1 = val1*10+ans1
        for i in num2:
            ans1 = dict1[i]
            val2 = val2*10+ans1
        product = val1*val2
        
        res=''
        while product>0:
            num = product%10
            for i in dict1:
                if num == dict1[i]:
                    res = i+res
            product = product//10 
        if res =="":
            return '0'
        else:     
            return res        






        