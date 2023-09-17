class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        ul = []
        i = head1
        j = head2
        while(i != None):
            ul.append(i.data)
            i = i.next
        while(j != None):
            ul.append(j.data)
            j = j.next
        ul = list(set(ul))
        ul.sort()
        ull = linkedList()
        for l in ul:
            ull.insert(l)
        return ull.head
        
        