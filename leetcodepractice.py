'''def division(dividend,divisor):
    res=dividend/divisor
    return round(res)
dividend,divisor=7,-3
print(division(dividend,divisor))

def reverse(n):
    string = str(n)
    reversed_num=string[::-1]
    return reversed_num
    
n='4568921'
print(reverse(n))

 
n=43261596
b=format(n,'032b')
print(b)
print(b.count('1'))
string_num=str(b)
reversed_num=string_num[::-1]
print(reversed_num)
result=int(reversed_num,2)
print(result)


n="abcd"
res=0

for letters in n:
    res+=ord(letters)
     
    sum1=res
print("n sum",sum1)
n="abcde"
res1=0
for letters in n:
    ascii_values=ord(letters)
    res1+=ascii_values
    sum2=res1
print("n1 sum",sum2)
difference=abs(sum1-sum2)
print("the difference is",difference)
print(chr(difference))



left=10
right=15
nums=[]
for i in range(left,right+1):    
    nums.append(i)
print(nums)
binary_vales=""
res=[]
for i in nums:
    binary_values = format(i,'b')
    res.append(binary_values)
print(res)
cnt=0
ans=0
for i in res:
    count_one=i.count('1')
    if count_one in  [2, 3, 5, 7, 11, 13, 17 ,19]:
        ans+=1
print("the count of ones:",ans)

#8 4 2 1
#0 1 0 1(5)
#0 1 1 1(7)
#--------
#0 1 0 1(5&7)

x=5
y=7
res=x
for i in range(x+1,y+1):
    print(i)
    res &=i
print(res)

 
arr=[1,1,1,1,1]
k=2
print("sum is:",sum(arr[:k]))


n=28
res=[]
for i in range(1,n):
    if n%i==0:
        res.append(i)
print(res)
if sum(res)==n:
    print(True)
else:
    print(False)'''


#EASY QUESTIONS
 
def twoSum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
arr=[10,20,30,5]
target=15
print(twoSum(arr,target))

def twoSumIndex(arr,target):
    low=0
    high=len(arr)-1
    while low<high:
        curr_sum=arr[low]+arr[high]
        if curr_sum==target:
            return [low+1,high+1]
        elif curr_sum<target:
            low+=1
        else:
            high+=1
arr=[10,20,30,5]
target=15
print(twoSumIndex(arr,target))

def perfectSquare(num):
    low=1
    high=num
    while low<=high:
        mid=(low+high)//2
        square=mid*mid
        if square==num:
            return True
        elif square<num:
            low=mid+1
        else:
            high=mid-1
    return False
num=14
print(perfectSquare(num))

def searchInsertPosition(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low
arr=[1,3,5,6]
target=2
print(searchInsertPosition(arr,target))

def plusone(arr):
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<9:
            arr[i]+=1
            return arr
        arr[i]=0
        return [1]+arr
arr=[1,2,3]
print(plusone(arr))

def pascalTriangle(arr):
    res=[]
    for i in range(arr):
        r=[1]*(i+1)
        for j in range(1,i):
            r[j]=res[i-1][j-1]+res[i-1][j]
             
        res.append(r)
    return res
arr=5
print(pascalTriangle(arr))

'''num=5
for i in range(num):
    r=[1]*(i+1)
    print(r)'''


nums=[2,6,7,9,1]
nums1=[4,8,9,2,12]
print("merged sorted array is:",set(sorted(nums+nums1)))

#def mergedSortedArray(m,n,nums1,nums2):

def bestTimeToSellStock(prices):
    minp=float('inf')
    maxp=0
    for price in prices:
        minp=min(price,minp)
        maxp=max(price-minp,maxp)
    return maxp
prices=[7,1,5,3,6,4]
print(bestTimeToSellStock(prices))

def majorityElement(arr):
    target=None
    count=0
    n=len(arr)
    for i in arr:
        if count==0:
            target=i
            count=1
        elif i==target:
            count+=1
        else:
            count-=1
    count=arr.count(target)
    if count>n/2:
        return target
    else:
        return -1
arr=[3,2,3]
print(majorityElement(arr))        


def containsDuplicate(nums):
    return len(nums)==len(set(nums))
nums=[1,2,3,1]
print(containsDuplicate(nums))

def missingNumber(nums):
    n=len(nums)
    original_sum=n*(n+1)//2
    
    missing_number=original_sum- sum(nums)
    return missing_number
nums=[0,1,2,3,4,6]
print(missingNumber(nums))

def moveZero(nums):
    res=[]
    zero_count=0
    for i in nums:
        if i !=0:
            res.append(i)
        else:
            zero_count+=1
        
    res.extend([0]*zero_count)
    return res
nums=[1,0,2,0,3,0]
print(moveZero(nums))


from collections import deque
def palindrome(num):
    dq=deque(str(num))
    while dq:
        return dq.popleft()==dq.pop()
num=12121213
print(palindrome(num))

 
'''def longestCommonPrefix(s):
    left=0
    d=deque()
    longest=0
    for right in range(len(s)):'''
def validParanthesis(s):
    left="[{("
    right="]})"
    res=[]
    for par in s:
        if par in left:
            res.append(par)
        if par in right:
            if right.index(par) != left.index(res.pop()):
                return False

    return True
s="{]"
print(validParanthesis(s))

def validAnagram(s,f):
    return sorted(s)==sorted(f)
s="anagram"
f= "nagaram"
print(validAnagram(s,f))

def validpalindrome(s):
    clean=""
    for char in s:
        if char.isalnum():
            clean+=char.lower()
    return clean==clean[::-1]
s = "A man, a plan, a canal: Panama"
print(validpalindrome(s))

def lenOfLastWord(sen):
    s=sen.split()
    if s:
        return len(s[-1])
sen='hello world'
print(lenOfLastWord(sen))
        
def removeElement(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k]=nums[i]
            k+=1
    return k
nums=[3,2,2,3,4]
val=3
print(removeElement(nums,val))

def romanToInteger(s):
    romans={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
    total=0
    prev_val=0
    for char in reversed(s):
        value=romans[char]
        if value<prev_val:
            total-=value
        else:
            total+=value
        prev_val=value
    return total
s="LVVVIII"
print(romanToInteger(s))


def longestPrefix(strs):
    prefix=""
    for i in range(min(len(s) for s in strs)):
        char=strs[0][i]
        if all(s[i]==char for s in strs):
            prefix += char
        else:
            break
    return prefix
strs=["flower","flow","flight"]
print(longestPrefix(strs))

def occuranceOfFirstIndex(haystack,needle):
    if needle=="":
        return 0
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1
haystack="leetcode"
needle="leeto"
print(occuranceOfFirstIndex(haystack,needle))


def reverseVowels(strs):
    vowels=set("aeiouAEIOU")
    left=0
    right=len(strs)-1
    s=list(strs)
    while left<right:
        while left<right and s[left] not in vowels:
            left+=1
        while left<right and s[right] not in vowels:
            right-=1
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return ''.join(s)
strs="leetcode"
print(reverseVowels(strs))
        
def power(n):
    if n<=0:
        return False
    while n%2==0: #n%3==0 , n%4==0
        n=n//2 #n//=3, n//=4
    return n==1
n=16
print(power(n))


def reverseInteger(n):
    sign=-1 if n<0 else 1
    reversed_n=int(str(abs(n))[::-1])*sign
    return reversed_n if -2**31<=reversed_n<=2**31 -1 else 1
n=-123
print(reverseInteger(n))

def addBinary(a,b):
    return bin(int(a,2)+int(b,2))[2:]
a='11'
b='1'
print(addBinary(a,b))

def setbits(n):
    set_bits=format(n,'032b')
    return set_bits.count('1')
n=11
print(setbits(n))

def climbingStairs(n):
    memo=[0]*(n+1)
    def helper(n):
        if n==1:
            return 1
        if n==2:
            return 2
        if memo[n]!=0:
            return memo[n]
        memo[n]=helper(n-1)*helper(n-2)
        return memo[n]
    return helper(n)
n=2
print(climbingStairs(n))
    
def fibannaci(n):
    memo=[0]*(n+1)
    def helper(n):
        if n==0:
            return 1
        if n==1:
            return 1
        if memo[n]!=0:
            return memo[n]
        memo[n]=helper(n-1)+helper(n-2)
        return memo[n]
    return helper(n)
n=2
print(fibannaci(n))
 
def isSubsequent(s,t):
    i=0
    j=0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==len(s)

'''s="abc"
t="ahbgdc"
print(isSubsequent(s,t))

 STACKS AND QUEUES class myQueue:
    def __init__(self):
        self.s=[]
    def enqueue(self,x):
        self.s.append(x)
    def dequeue(self):
        if not self.s:
            return -1
        x=self.s.pop()
        if not self.s:
            return
        self.dequeue()
        self.s.append(x)
        return
    def peek(self):
        if not self.s:
            return -1
        x=self.s.pop()
        if not self.s:
            return
        item=self.peek()
        self.s.append(x)
        return item
    def size(self):
        return len(self.s)
    def __str__(self):
        return str(self.s[::-1])
    
   
        
if __name__=="__main__":
    s=myQueue()
    s.enqueue(10)
    s.enqueue(20)
    s.enqueue(30)
    print(s)
    print(s.dequeue())
    print(s.peek())
    print(s.size())

from collections import deque    
class myStack:
    def __init__(self):
        self.q=deque()
    def push(self,x):
        self.q.append(x)
        size=len(self.q)
        for i in range(size-1):
            self.q.append(self.q[0])
            self.q.popleft()
    def pop(self):
        if self.q:
            self.q.popleft()
    def peek(self):
        if self.q:
            return self.q[0]
    def empty(self):
        return len(self.q)==0
    def __str__(self):
        return str(self.s[::-1]) 
if __name__=="__main__":
    s=myStack()
    s.push(1)
    s.push(2)
    s.push(4)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s.empty())

 LINKED LIST    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def singleLinkedList(self):
        self.head=None
    def insertHead(self,x):
         newNode=Node(x)
         newNode.next=self.head
         self.head=newNode
         return newNode
    def insertEnd(self,x):
        newNode=Node(x)
        if self.head is None:
            return -1
        curr=self.head
        while curr:
            curr=curr.next
        curr.next=newNode
        return curr
    def display(self):
        curr=self.head
        if curr is None:
            return False
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("None")
    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        self.head=prev
    def isplaindrome(self):
        stack=[]
        slow=fast=self.head
        while fast and fast.next:
            stack.append(slow.data)
            fast=fast.next.next
            slow=slow.next
        if fast:
            slow=slow.next
        while slow:
            if slow.pop != slow.data:
                return False
            slow==slow.next
        return True
    def removeDuplicates(self):
        seen=set()
        res=[]
        curr=self.head
        while curr:
            if curr.data not in seen:
                seen.add(curr.data)
                res.append(curr)
            curr=curr.next
        return curr
            
    def cycle(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
            else:
                return False
            
    def removeElements(self,val):
        dummy=Node(0)
        dummy.next=self.head
        curr=dummy
        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next 
    
from itertools import permutations
arr=[1,2,3]
s=permutations(arr)
print(s)
 def permutation(s):
    return sorted(set(''.join(s1) for s1 in permutations(s)))
s="ab"
print(permutations(s))'''

arr=[7,8,9,5,6,6]
arr1=sorted(set(arr))
rev_arr=list(reversed(arr1))
print(rev_arr[1])


    
        
