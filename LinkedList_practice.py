class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:

    def __init__(self):
        self.head=None

        
    def insert(self,x):
        newNode=Node(x)
        newNode.next=self.head
        self.head=newNode
        return newNode

    
    def insertend(self,x):
        newNode=Node(x)
        if self.head is None:
            return -1
        last=self.head
        while last.next is not None:
            last=last.next
        last.next=newNode# it traverses till the last node and inserts the newnode at last.next
        return last
    
    def insertpos(self,x,pos):
        if pos<1:
            return False
        #case 1:insert at head
        if pos==1:
            newNode=Node(x)
            newNode.next=self.head
            self.head=newNode
            return newNode
        #case 2: insert at pos >1
        curr=self.head
        for i in range(1,pos-1):
            if curr is not None:
                curr=curr.next
            else:
                return False #position out of bounds
        #base case for every method
        if curr is None:
            return False
        #[1]-[2]-[3]-[4]
        # 0   1   2   3(index)
        #if we want to insert at 2
        #loop will iterate till (1)
        #curr=[2]
        #curr.next=[3],node is currently at index 3
        #newNode will be added b/w [2] & [3]
        newNode=Node(x)
        newNode.next=curr.next  
        curr.next=newNode
        return True
    def display(self):
        curr=self.head
        if curr is None:
            return False
        else:
            while curr:
                print([curr.data],end=" -> ")
                curr=curr.next
            print("None")

    def deleteatbeg(self):
        self.head
        if self.head is not None:
            self.head=self.head.next
            return self.head
        return None

    def deleteatend(self):
        curr=self.head
        if curr is None:
            return None
        while curr.next.next is not None:
            curr=curr.next
        curr.next=None
        return curr

    def deleteatpos(self,pos):
        if pos==1:
            self.head=self.head.next
            return self.head
        curr=self.head
        for i in range(1,pos-2):
            curr=curr.next
        curr.next=None
        return curr

        if curr is None:
            return False

    def search(self,key):
        if self.head is None:
            return None
        curr=self.head
        while curr:
            if curr.data==key:
                print("key is found")
                return True
            curr=curr.next
        print("key is not found")
        return False

    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
        #[1]->[2]->[3]->[4]->[5]->[6]->None
        #curr=2
        #prev=1
        #here in every iteration the values will get stored in prev
        #prev=[1]->[2]->[3]->[4]->[5]->[6]

    def middle(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data if slow else None

    def oddeven(self):
        curr=self.head
        while curr:
            if curr.data%2==0:
                print([curr.data],"even")
            else:
                print([curr.data],"odd")
            curr=curr.next
    def oddevenindex(self):
        #[6]->[5]->[4]->[3]->[2]->[1]->None
        # 0    1    2    3    4    5    6
        #we have to group all the nodes with odd indexes together followed by even indexs
        # we have to print Input: head = [1,2,3,4,5] Output: [1,3,5,2,4]
        #                                 0 1 2 3 4           0 2 4 1 3
        #[2,1,3,5,6,4,7] Output: [2,3,6,7,1,5,4]
        # 0 1 2 3 4 5 6           0 2 4 6 1 3 5
        #for the input [6]->[5]->[4]->[3]->[2]->[1] the output should be [6]->[4]->[2]->None->[5]->[3]->[1]
        curr=self.head
        indexed_node=[]
        while curr:
            indexed_node.append(curr.data)
            curr=curr.next
      
        even=[]
        odd=[]
        for i in range(len(indexed_node)):
            if i%2==0:
                even.append(indexed_node[i])
            else:
                odd.append(indexed_node[i])
        res=even+odd
        return res

    def sortlist(self, head):
        if not head or not head.next:
            return head

    # Step 1: Find the middle
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev.next = None  # Split the list into two halves

    # Step 2: Recursively sort both halves
        left = self.sortlist(head)
        right = self.sortlist(mid)

    # Step 3: Merge sorted halves
        return self.merge(left, right)

    def merge(self,l1,l2):
        dummy=Node(0)
        tail=dummy
        while l1 and l2:
            if l1.data<l2.data:
                tail.next,l1=l1,l1.next # this line is tuple unpacking to perform 2 tasks simulteniously
                    #the above code is explained as tail.next = l1
                    #                               l1 = l1.next
            else:
                tail.next,l2=l2,l2.next
            tail=tail.next
        tail.next=l1 or l2
        return dummy.next
            
        
if __name__=='__main__':
    sll=SingleLinkedList()
    sll.insert(1)
    sll.insertend(2) 
    sll.insertpos(3,1)
    sll.insertpos(5,3)
    sll.display() # [3]->[1]->[5]->[2]->None
    sll.deleteatbeg()
    sll.display()#[1]->[5]->[2]->None
    sll.deleteatend()
    sll.display()#[1]->[5]->None
    sll.deleteatpos(2)
    sll.display()#[1]->None
    sll.insertend(2)
    sll.insertend(3)
    sll.insertend(4)
    sll.insertend(5)
    sll.insertend(6)
    sll.display()#[1]->[2]->[3]->[4]->[5]->[6]->None
    sll.search(4)
    sll.search(100)
    sll.reverse()
    sll.display()#[6]->[5]->[4]->[3]->[2]->[1]->None
    print("the middle element is:",[sll.middle()])#the middle element is: [3]
    print(sll.oddeven())#[6] even
                        #[5] odd
                        #[4] even
                        #[3] odd
                        #[2] even
                        #[1] odd
                        #None
    print(sll.oddevenindex())#[6, 4, 2, 5, 3, 1]
    sll.head=sll.sortlist(sll.head)
    sll.display()
