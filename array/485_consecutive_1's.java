// class Solution:
//     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

//        count=0
//        maxi=0
//        for i in range(len(nums)):
//            if nums[i]==1:
//                count+=1
//                maxi=max(count,maxi)
//            else:
//                 count=0
//        return maxi           


class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        int count=0;
        int maxi=0;
        for(int i=0;i<nums.length;i++){
            if (nums[i]==1){
                count++;
                maxi=Math.max(maxi,count);
            }
            else{
                count=0;
            }
        }
        return maxi;
        
    }
}