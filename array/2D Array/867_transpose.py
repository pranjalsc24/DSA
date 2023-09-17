class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return [e for e in zip(*matrix)]
        
        
        # below code gives transpose but all the tst cases are not passing
        # for i in range(len(matrix)):
        #     for j in range(i+1,len(matrix)):
                
        #         temp=matrix[i][j]
        #         matrix[i][j]=matrix[j][i]
        #         matrix[j][i]=temp

        # return matrix 

            
            