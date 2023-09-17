# binary seaarch
# Find Smallest Letter Greater Than Target

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low=0
        high=len(letters)-1

        while (low<=high):

            mid=(low+high)//2

            if letters[mid]<target:
                low=mid+1
            else:
                high= mid-1
        return letters[low%len(letters)]        

        # if low<len(letters):
        #     return letters[low]
        # return letters[0]    


# min1 = target
        # for i in letters:
        #     if i>min1:
        #         min1 = i
        #         break
        # if min1==target:
        #     return letters[0]
        # return min1



# -------------------in java-------------------

# class Solution {
#     public char nextGreatestLetter(char[] letters, char target) {

#         int low=0;
#         int high = letters.length-1;

#         while(low<=high){
#             int mid=low+(high-low)/2;
            
#             if(target < letters[mid]){
#                 high= mid -1;
#             }
#             else  {
#                 low=mid+1;
#             }
           
#         }
#         return letters[low % letters.length];
#         }
# }
