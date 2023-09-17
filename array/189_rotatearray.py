# # https://www.youtube.com/watch?v=BHr381Guz3Y&ab_channel=NeetCode

# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)

#         # In case if k is greater than the no. of elements in array. e.g rotate [1,2] by 3 places
#         # We get [2,1]. which is the same as rotating it once. Hence k = k % n
#         if k > n:
#             k = k % n 

#         # to reverse the whole array
#         a = 0
#         b = n - 1

#         while a <= b:
#             nums[a], nums[b] = nums[b], nums[a]
#             a += 1
#             b -= 1

        
#         # to reverse the first k elements
#         a = 0
#         b = k - 1

#         while a <= b:
#             nums[a], nums[b] = nums[b], nums[a]
#             a += 1
#             b -= 1

#         # to reverse the remaining elements after k 
#         a = k
#         b = n - 1

#         while a <= b:
#             nums[a], nums[b] = nums[b], nums[a]
#             a += 1
#             b -= 1



# # for rotating one position
def rotate(arr):
    n=len(arr)
    i=n-1
    j=n-2
    temp=arr[n-1]
    while j>=0:
        arr[i]=arr[j]
        i-=1
        j-=1  

    arr[0]=temp
    return arr

arr = [10, 324, 45, 90, 9808] 
Ans = rotate(arr)
print(Ans)   


# =-----------java-------

# class Solution {
#     public void rotate(int[] arr, int k) {
#      int  n=arr.length;
#       if (k>n){
#         k=k%n;
#      }
#         reverse(arr,0,n-1);
#         reverse(arr,0,k-1);
#         reverse(arr,k,n-1);
#   }
 

#     void reverse(int[] arr,int start,int end){
#       while(start<=end){
#         int temp=arr[start];
#         arr[start]=arr[end];
#         arr[end]=temp;
#         start++;
#         end--;
#       }
      
#     }
# }




