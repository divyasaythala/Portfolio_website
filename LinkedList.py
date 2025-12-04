#single linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singleLinkedList:
    def __init__(self):
        self.head=None


    #displaying linkedlist   
    def display(self):
        curr=self.head
        if curr is None:
            print("empty")
        else:
            while curr:
                print(curr.data,end="->")
                curr=curr.next
            print("None")


    #insert at the front       
    def insertAtFront(self,x):
        newNode=Node(x)
        newNode.next=self.head
        self.head=newNode


    # insert at the back
    def insertAtEnd(self,x):
        newNode=Node(x)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
        return self.head



    #insert at the specific position
    def insertAtPos(self,x,pos):
        if self.head is None:
            print("empty")
        newNode=Node(x)
        if pos==1:
            newNode.next=self.head
            self.head=newNode
            return
        curr=self.head
        for _ in range(pos-2):
            if curr is None:
                return head
            curr=curr.next
        newNode.next=curr.next
        curr.next=newNode



    #delete at the front
    def deleteHead(self):
        if self.head is None:
            print("empty")
            return
        self.head=self.head.next



    #delete at the end
    def deleteAtEnd(self):
        if not self.head or not self.head.next:
            self.head=None
            return
        curr=self.head
        while curr.next.next:
            curr=curr.next
        curr.next=None



    #delete at the specific position
    def deleteAtPos(self,pos):
        if pos==1:
            self.head=self.head.next
            return 
        curr=self.head
        for _ in range(pos-2):
            if not curr or not curr.next:
                print("position out of bounds")
                return
            curr=curr.next
        curr.next=curr.next.next



    #search for a key in linkedlist
    def searching(self,key):
        curr=self.head
        while curr is not None:
            if curr.data==key:
                return True
            curr=curr.next
        return False


    #reverse of linkedlist
    def reverse(self):
        curr=self.head
        prev=None
        while curr is not None:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        self.head=prev



    #clear
    def clear(self):
        self.head=None


    #length of linkedlist
    def size(self):
        curr=self.head
        size=1
        while curr is not None:
            size+=1
            curr=curr.next
        return size


    #tostring()
    def tostring(self):
        res=[]
        curr=self.head
        while curr:
            res.append(str(curr.data))
            curr=curr.next
        return res


    #get position
    def getPosition(self,x):
        curr=self.head
        index=0
        while curr:
            if curr.data==x:
                return index
            curr=curr.next
            index+=1
        return -1


    #check is palindrome
    def isPalindrome(self):
        stack=[]
        slow,fast=self.head,self.head# two pointers to traverse till middle
        while fast and fast.next:
            stack.append(slow.data)
            slow=slow.next
            fast=fast.next.next # stack stores till middle value
        if fast:
            slow=slow.next # second half begins, skip middle if it is odd
        while slow: #comparing secong half with first 
            if stack.pop() != slow.data:
                return False
            slow=slow.next
        return True


    #copy list in another list
    def copy(self):
        if self.head is None:
            return None
        secondList=singleLinkedList()
        curr=self.head
        secondList.head=Node(curr.data)
        newcurr=secondList.head
        curr=curr.next
        while curr:
            newcurr.next=Node(curr.data)
            newcurr=newcurr.next
            curr=curr.next
        return secondList
               

    #remove duplcate
    def removeDuplicate(self):
        seen=set()
        res=[]
        curr=self.head
        while curr:
            if curr.data not in seen:
                seen.add(curr.data)
                res.append(curr)#res.append(curr.data)
            curr=curr.next
        return res



    #merge with aother list
    def merge(self,secondList):
        #append second list to the curr list
        if not self.head:
            self.head=secondList.head
            return
        curr=self.head
        while curr:
            curr=curr.next
        curr.next=secondList.head

        
    #move the second node to the head
    def move(self):
        if self.head and self.head.next:
            second=self.head.next #a->b->c---second=b
            self.head.next=second.next#self.head.next=c
            second.next=self.head#second.next=a
            self.head=second#b->a->c
 


    #find the middle of linkedList
    def middle(self):
        #tortoise-hare method is used
        slow=fast=self.head
        while fast and fast.next:
            fast=fast.next.next
            if fast:
                slow=slow.next
        return slow.data if slow else None


    #find n from the end
    def findn(self,n):
        #two pinters approach
        first=second=self.head
        for _ in range(n):
            if not first:
                return None
            first=first.next
        while first:
            first=first.next
            second=second.next
        return second.data if second else None
        #a->b->c->d->e  [1]-[2]-[3]-[4]
        #for loop: first second 
        #           b      a    2   1
        #           c      a    3   1
        #while loop: first second
        #             d     b   4    2
        #             e     c   None 3
        #           None    d return d
        # n=2 so first will move n steps ahead 


'''DETECT CYCLE'''
    #detect cycle
    def detectCycle(self):
        #flyod cylce detection
        slow=fast=self.head
        while fast and fast.next: 
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    # a->b->c->d->e
    #       |___|      
    #from e we can see a cycle
    #slow fast
    # b    c   (no)
    # c    e   (no)
    # d    d   (yes)
    #cycle is detected

    #MAIN METHOD
def test_all_methods():
    sll = singleLinkedList()
    sll.head = Node('A')
    sll.head.next = Node('B')
    sll.head.next.next = Node('C')
    sll.head.next.next.next = Node('B')
    sll.head.next.next.next.next = Node('A')

    sll.insertAtFront('D')
    sll.insertAtEnd('E')
    sll.insertAtPos('F', 2)
    sll.deleteHead()
    sll.deleteAtEnd()
    sll.deleteAtPos(2)
    sll.display()
    print(sll.tostring())
    print(sll.size())
    sll.clear()
    sll.display()

    # Rebuild list for further tests
    for val in ['A', 'B', 'C', 'B', 'A']:
        sll.insertAtEnd(val)

    print("Middle:", sll.middle())
    print("Cycle Detected:", sll.detectCycle())
    print("2nd from end:", sll.findn(2))
    sll.move()
    sll.display()

    # Merge test
    second = singleLinkedList()
    for val in ['X', 'Y', 'Z']:
        second.insertAtEnd(val)
    sll.merge(second)
    sll.display()

    print("Duplicates removed:", [node.data for node in sll.removeDuplicate()])
    copied = sll.copy()
    print("Copied list:")
    copied.display()

    print("Is Palindrome:", sll.isPalindrome())
    print("Position of 'C':", sll.getPosition('C'))
    sll.reverse()
    sll.display()
    print("Search 'X':", sll.searching('X'))

test_all_methods()     
