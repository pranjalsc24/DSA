# Length of Last Word

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        


# strip()
# Remove spaces at the beginning and at the end of the string:

# split()
# Split a string into a list where each word is a list item

# ---------- easy way---------------
        # res=s.split( )
        # return len(res[-1])


        # --------- another solution----

        i=len(s)-1
        count=0

        while s[i]==" ":
            i -= 1
        while i>=0 and s[i] != " ":
            count +=1
            i -=1

        return count        


        # ---------- another -----
        #  -----wrong approch---

        # count=0
        # i=len(s)-1

        # while s!=0:
        #     if s[i]==" ":
        #         i -= 1
        #     elif i>=0 and s[i] !=" ":
        #         count+=1
        #         i -= 1
        # return count        



    



      


