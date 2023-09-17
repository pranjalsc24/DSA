# creating linkedlist

class Node:
    def __init__(self,data):

       self.data=data
       self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--->",end=" ")
                temp=temp.next    


L=singlelinkedlist()
n1= Node(10)
L.head=n1
n2=Node(20)
# L.head.next=n2  -----og
n1.next=n2   # changed by me
n3=Node(30)
n2.next=n3
L.display()



