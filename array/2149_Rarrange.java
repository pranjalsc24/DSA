// striver
// --------brute----------

// // class Solution {
// //     public int[] rearrangeArray(int[] A) {
// //         int n=A.length;
// //          ArrayList<Integer> pos=new ArrayList<>();
// //          ArrayList<Integer> neg=new ArrayList<>();
  
// //   // Segregate the array into positives and negatives.
// //   for(int i=0;i<n;i++){
      
// //       if(A[i]>0) pos.add(A[i]);
// //       else neg.add(A[i]);
// //   }
  
// //   // Positives on even indices, negatives on odd.
// //   for(int i=0;i<n/2;i++){
      
// //       A[2*i] = pos.get(i);
// //       A[2*i+1] = neg.get(i);
// //   }

 
// //   return A;
// //     }
// // }


// // --------optimal----------
// class Solution {
//     public int[] rearrangeArray(int[] nums) {
//       int[] ans=new int[nums.length];
//       int pos=0;
//       int neg=1;
//       for(int i=0;i<nums.length;i++){
//           if(nums[i]>0){
//           ans[pos]=nums[i];
//           pos+=2;
//           }
//       else{
//           ans[neg]=nums[i];
//           neg+=2;
//       }
//       }
//       return ans;

//     }
//  }



