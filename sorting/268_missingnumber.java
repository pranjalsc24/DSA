// Example 1:

// Input: nums = [3,0,1]
// Output: 2
// Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.



// // kunal
// // cyclic sort

// class Solution {
//     public int missingNumber(int[] arr) {
//         // sorting the array 
//       int i=0;
//       while(i<arr.length){
//           int correct=arr[i];

//           if (arr[i]<arr.length && arr[i]!=arr[correct]){
//               swap(arr,i,correct);
//           }
//           else{
//             i++;
//           }
//       }

//     //   search the elemnt in arrau
//     for(int index=0;index<arr.length;index++){
//         if(arr[index] != index){
//             return index;
//         }
//     }
//     return arr.length;

        
//     }

//     static void swap(int[] arr, int first, int second) {
//         int temp = arr[first];
//         arr[first] = arr[second];
//         arr[second] = temp;
//     }


// }


// -------------python-----------------

// class Solution(object):
//     def missingNumber(self, nums):
//         """
//         :type nums: List[int]
//         :rtype: int
//         """
//         nums.sort()

//         # if len(nums)==1 and nums[0]==1:
//         #     return 0

//         if 0 not in nums:
//             return 0

       
//         maxx=0
//         for i in range(len(nums)):
            
//             if nums[i]==maxx:
//                 maxx+=1
            
            


//         return maxx