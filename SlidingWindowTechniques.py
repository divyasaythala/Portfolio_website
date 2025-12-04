'''FIXED SIZE'''


 #maximum sum of distinct subarray of size k
from collections import deque
def slidingwindow(nums,k):
    d=deque() #stores indices
    res=[]
    for i in range(len(nums)):
        '''step1: remove indices that are out of this window'''
        if d and d[0]<i-k+1: ''''peekFirst=dq[0],peekLast=dq[-1] as it is the double ended queue we can insert and remove at the both ends'''
        #if d is not isEmpty and dq of peekFirst<i-k+1
            d.popleft()
            #dq.removeFirst
        '''STEP-2: remove smaller numbers from the back because they can never be maximum if a bigger number is coming in'''
        while d and nums[d[-1]]<nums[i]:
        # while d in not empty and nums[dq.peekLeft()]<nums[i]
            d.pop()
            #d.popLast
        '''STEP-3:add current element's index'''
        d.append(i)
        '''STEP-4:if we have processed at least k elements,record the max'''
        if i>=k-1:
            res.append(nums[d[0]])
    return res
nums=[-1,3,1,-3,5,3,6,7]
k=3
print(slidingwindow(nums,k))




#fisrt negative number in every window of size k





#count occurance of anagram






#find all anagrams
def findanagrams(s,f):
    s_count=Counter()
    f_count=Counter(f)
    



'''VARIABLE SIZE'''
#smallest subarray sum>=target







#longest substring with out repeating characters
def longest(s):
    long=0
    l=0
    s1=set()
    for r in range(len(s)):
        while s[r]in s1:
            s1.remove(s[l])
            l+=1
        w=(r-l)+1
        long=max(long,w)
        s1.add(s[r])
    return long
s="abcabcbb"
print(longest(s))
#subarray sum equals to k
from collections import defaultdict
def subarraysum(nums,k):
    count=0
    curr_sum=0
    prefix_sum=defaultdict(int)
    prefix_sum[0]=1
    for num in nums:
        curr_sum+=num
        count+=prefix_sum[curr_sum-k]
        prefix_sum[curr_sum]+=1
    return count
nums=[1,2,3]
k=3
print(subarraysum(nums,k))
    



#min no. of operation to reduce x to zero
