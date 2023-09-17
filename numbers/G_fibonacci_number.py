class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        first = 0
        second = 1
        third = 1
        lis = []
        for i in range(n):
            lis.append(third)
            third = first + second
            first = second
            second = third
        return lis

        
