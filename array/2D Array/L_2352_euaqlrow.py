# 2352. Equal Row and Column Pairs

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dict1 = {}
        count = 0
        for i in range(len(grid)):
            if tuple(grid[i]) not in dict1:
                dict1[tuple(grid[i])]=1
            elif tuple(grid[i]) in dict1:
                dict1[tuple(grid[i])]=dict1[tuple(grid[i])]+1
        # print dict1
        for j in range(len(grid)):
            list1 = []
            for k in range(len(grid)):
                list1.append(grid[k][j])
            if tuple(list1) in dict1:
                count += dict1[tuple(list1)]
                list1 = []
        return count  

#    =------------ but this is not optimal because it tokk n^3 time
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid)):
        #         flag = 1
        #         for k in range(len(grid)):
        #             if grid[i][k]!=grid[k][j]:
        #                 flag =0 
        #                 break
        #             else:
        #                 continue

        #         count=count + flag
        # return count
