def lengthOfLongestSubstring( s):

        char= set()
        l=0
        res=0

        

        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l=l+1
            char.add(s[r])    
            res=max(res,r-l+1)

        return res  

print(lengthOfLongestSubstring("abcabcbb"))  