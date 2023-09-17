// https://www.youtube.com/watch?v=5qGrJbHhqFs&ab_channel=takeUforward


class Solution {
    public int search(int[] nums, int target) {

        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            int middle = (left+right)/ 2;
            System.out.println(middle);
            
            if (nums[middle] == target) return middle;
               
            
            if (nums[middle] >= nums[left]) {
                if (nums[left] <= target && target < nums[middle]) {
                    right = middle - 1;
                } 
                else {
                    left = middle + 1;
                }
            } else {
                if (nums[middle] < target && target <= nums[right]) {
                    left = middle + 1;
                } else {
                    right = middle - 1;
                }
            }
        }
        
        return -1;




// --------------below is for linear seach--------------------

        // for(int i=0;i<nums.length;i++){
        //     if (nums[i]==target){
        //         return i;
        //     }
            
        // }
        // return -1;

        
    }
}