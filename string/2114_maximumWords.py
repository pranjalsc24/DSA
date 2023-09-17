# Maximum Number of Words Found in Sentences

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        # return max(len(word.split()) for word in sentences)

        count=0
        for i in sentences:
            x=i.count(' ')+1
            if x>count:
                count=x
        return count
        