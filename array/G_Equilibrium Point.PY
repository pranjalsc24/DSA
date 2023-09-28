def equilibriumPoint(self,A, N):
        # Your code here
        total_sum = sum(A)
        
        left_sum = 0
        
        for i in range(N):
            # Subtract the current element from the total sum to get the right sum
            right_sum = total_sum - left_sum - A[i]
            
            if left_sum == right_sum:
                return i + 1  # Equilibrium point found at index i+1 (1-based index)
            
            left_sum += A[i]
        
        return -1  # If no equilibrium point is found


# class Solution {

    
#     // a: input array
#     // n: size of array
#     // Function to find equilibrium point in the array.
#     public static int equilibriumPoint(long[] A, int N) {

#         // Your code here
#         long totalSum = 0;
#         for (int i = 0; i < N; i++) {
#             totalSum += A[i];
#         }

#         long leftSum = 0;

#         for (int i = 0; i < N; i++) {
#             // Subtract the current element from the total sum to get the right sum
#             long rightSum = totalSum - leftSum - A[i];

#             if (leftSum == rightSum) {
#                 return i + 1;  // Equilibrium point found at index i+1 (1-based index)
#             }

#             leftSum += A[i];
#         }

#        return -1; 
#     }
# }
