// // kunal 
// // cyclic


// class Solution {
//     public int findDuplicate(int[] arr) {
//         int i = 0;
//         while (i < arr.length) {
//             int correct = arr[i];
//             if (arr[i] != arr[correct]) {
//                 swap(arr, i , correct);
//             } else {
//                 i++;
//             }
//         }

//         for(int index=0;index<arr.length;index++){
//         if(arr[index] != index){
//             return arr[index];
//         }
//     }
//     return 0;
        
//     }

//     static void swap(int[] arr, int first, int second) {
//         int temp = arr[first];
//         arr[first] = arr[second];
//         arr[second] = temp;
//     }
// }







// othe code can be also
// public int findDuplicate(int[] arr) {
//         int i = 0;
//         while (i < arr.length) {
//             if arr[i] != i+1;{
    //             int correct = arr[i];
    //             if (arr[i] != arr[correct]) {
    //                 swap(arr, i , correct);
    //             } else {
    //                return arr[i];
//                  }
//             else{
//                  i++;
//               }
//          }
             
//          }
//       return -1;
//     } 

//        
        
//     




