class Solution(object):
    def hammingWeight(self, n):
        count=0
        for i in range(str(len(n))):
            if(i==1):
                count+=1
        
        print(count)        
        

      