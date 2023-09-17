# class Solution:
#     def countOdds(self, low, high):
#         # Initialize odd with the number of even numbers between low and high.
#         odd = (high - low) // 2
        
#         # If either low or high is odd, increment odd by 1.
#         if low % 2 == 1 or high % 2 == 1:
#             odd += 1
        
#         # Return the number of odd numbers between low and high.
#         return odd



# -----------below solution is also right but memory exceeded------------------

def count(low,high):
    list=[]
    for i in range(low,high+1):
        if i%2!=0:
            list.append(i)
    return len(list)       

print(count(3,7))            