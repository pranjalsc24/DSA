// class Solution {
//     int getPairsCount(int[] arr, int n, int k) {
//         Map<Integer, Integer> occurance = new HashMap<Integer, Integer>();
//         int numberOfPairs = 0;
        
//         for(int i: arr) {
//             int target = k - i;
            
//             if(occurance.containsKey(target)) {
//                 numberOfPairs += occurance.get(target);
//             }
            
//             occurance.put(i, occurance.getOrDefault(i, 0) + 1);
//         }
        
//         return numberOfPairs;
//     }
// }