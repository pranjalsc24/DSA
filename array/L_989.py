#  Add to Array-Form of Integer
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        #  [2,7,4]  k=181 ------------>   example 

        # ------------- correct solution---------------
        # s=0
        # for i in num:
        #     s=s*10+i
        # s=s+k
        # lst=[]
        # while(s!=0):
        #     lst.append(s%10)
        #     s=s//10
        # return lst[::-1]

       
        n=len(num)
        i=n-1
        res=[]
        while(i>=0 or k>0):
            if(i>=0):
                res.append((num[i]+k)%10)
                k=(num[i]+k)/10
            else:
                res.append(k % 10)
                k /=10
            i=i-1
        return res[::-1]
       
       
       
       
       
       
       
        # ----------------- trial code------------------
        # res=[]
        # j=-1
        # s=0

        # for i in range(len(num)):
        #     add=num[j] + k                #add=4+181=185      next--- 7+18=25
        #     k=add//10                     # k=18                  --- k=2
        #     add=add % 10                  # add=5                 --- add=5 
        #     res.append(add)                # [5]                   [5,5] 
        #     j -=1

        # if k:
        #     res.append(k) 

        # return res[::-1]
        
        


       

               
                                   
            






       