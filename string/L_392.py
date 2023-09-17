# Input: s = "abc", t = "ahbgdc"
# Output: true

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # i=0
        # j=0

        # while(i<len(s) and j<len(t)):
        #     if s[i]==t[j]:
        #         i+=1
        #     else:
        #         j+=1
        # return i==len(s) 


        # ---------another-------------

        j = 0
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1
        return j == len(s)          


       
           


