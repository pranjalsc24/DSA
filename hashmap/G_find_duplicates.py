class Solution:
    def duplicates(self, arr, n): 
    	# code here
        result = []  # Use a different variable name

        map = {}
        for num in arr:
            map[num] = map.get(num, 0) + 1

        for key, value in map.items():
            if value > 1:
                result.append(key)  # Append the duplicate elements to result

        if len(result) == 0:
            return [-1]  # Return -1 when there are no duplicates
        else:
            return sorted(result)  # Return the list of duplicates in sorted order
        
# import java.util.ArrayList;
# import java.util.HashMap;
# import java.util.List;
# import java.util.Map;

# class Solution {
#     public static ArrayList<Integer> duplicates(int arr[], int n) {
#         // code here
#         List<Integer> res = new ArrayList<>();
#         Map<Integer, Integer> map = new HashMap<>();

#         for (int i = 0; i < n; i++) {
#             map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
#         }
        
#         for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
#             if (entry.getValue() > 1) {
#                 res.add(entry.getKey());
#             }
#         }

#         if (res.isEmpty()) {
#             res.add(-1);  // Return -1 as a single-element list
#         } else {
#             res.sort(null);  // Sort the list of duplicates
#         }

#         return res;
#     }

#     public static void main(String[] args) {
#         int[] arr = {2, 3, 1, 2, 3};
#         int n = arr.length;
#         ArrayList<Integer> duplicates = duplicates(arr, n);
#         System.out.println(duplicates);  // Output: [2, 3]
#     }
# }
        