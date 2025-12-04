class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None

    def insertatbeg(self,x):
        newnode=Node(x)
        newnode.next=self.head
        self.head=newnode
        return newnode

    def insertatend(self,x):
        newnode=Node(x)
        if self.head is None:
            return -1
        last=self.head
        #[1]-[2]
        #we want to add [3] at the end
        #last=[1]
        #last iteration - last=[2]
        #
        while last.next is not None:
            last=last.next
        last.next=newnode
        return last


    def insertatpos(self,x,pos):
        while pos<1:
            return False

        if pos==1:
            newnode=Node(x)
            newnode.next=self.head
            self.head=newnode
            return newnode
        curr=self.head
        for i in range(1,pos-1):
            if curr is not None:
                curr=curr.next
            else:
                return False

        if curr is None:
            return False

        newnode=Node(x)
        newnode.next=curr.next
        curr.next=newnode
        

    def display(self):
        curr=self.head
        if curr is None:
            return "empty"
        else:
            while curr:
                print(curr.data,end=" --> ")
                curr=curr.next
            print("None")
    def deleteatbeg(self):
        if self.head is not None:
            self.head=self.head.next
            return self.head
    def deleteatend(self):
        if self.head is None:
            return False
        curr=self.head
        while curr.next.next is not None:
            curr=curr.next
        curr.next=None
        return curr
    def deleteatpos(self,pos):
        if pos==1:
            self.head=self.head.next
            return self.head
        curr=self.head
        for i in range(1,pos-1):
            curr=curr.next
        curr.next=None
        return curr
        if curr is None:
            return False

if __name__=='__main__':
    sll=SingleLinkedList()
    sll.insertatbeg(1)
    sll.insertatend(3)
    sll.insertatpos(2,1)
    sll.insertatbeg(5)
    sll.display()#5-->2-->1-->3-->None 
    sll.deleteatbeg()
    sll.display()#2-->1-->3-->None
    sll.deleteatend()
    sll.display()#2-->1-->None
    sll.deleteatpos(1)
    sll.display()#1-->None
