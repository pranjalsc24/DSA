class Solution {
    public int maximumWealth(int[][] accounts) {
        
        int max=0;
        for(int row=0; row< accounts.length; row++){
            int rowsum=0;
            for(int col=0;col< accounts[row].length; col++ ){
                rowsum=rowsum+ accounts[row][col];

            }

            if (rowsum > max){
                max=rowsum;
            }


        }
        return max;

    }
}


// PYTHON

// class Solution(object):
//     def maximumWealth(self, accounts):
//         """
//         :type accounts: List[List[int]]
//         :rtype: int
//         """
//         max_wealth = 0
//         for i in range(len(accounts)):
//             max_wealth = max(sum(accounts[i]), max_wealth)
        
//         return max_wealth
        