# Isomorphic Strings

# Input: s = "egg", t = "add"
# Output: true

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # map1 = []
        # map2 = []
        # for i in s:
        #     map1.append(s.index(i))
        # for j in t:
        #     map2.append(t.index(j))

        # # print(map1)
        # # print(map2)

        # if map1 == map2:
        #     return True
        # return False

        # -----------another---------------
        
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))



