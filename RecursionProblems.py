#fibanocci
def fibanocci(n):
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
n=10
fib=fibanocci(n)
for _ in range(n):
    print(next(fib))






#all subsets
def subsets(nums):
    res=[]
    def dfs(index,path):
        res.append(path[:])
        for i in range(index,len(nums)):
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
    dfs(0,[])
    return res
nums=[1,2,3,4,5]
print(subsets(nums))






#power function
def power(x,n):
    return pow(x,n)
x=5
n=2
print(power(x,n))
#using recursion
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

x=5
n=2
print(power(x,n))




#print all elements using recurison
def printelements(nums,index=0):
    if index==len(nums):
        return
    print(nums[index])
    printelements(nums,index+1)
nums=[1,2,3,4]
print(printelements(nums,index=0))





#permutations
from itertools import permutations
def permutationsofnumber(s):
    return ["".join(p)for p in permutations(s)]
s="ABC"
print(permutationsofnumber(s))





#tower of hanoi
def towerofhanoi(n,src,dest,temp):
    if n>=1:
        towerofhanoi(n-1,src,temp,dest)
        print("Move %s->%s"%(src,dest))
        towerofhanoi(n-1,temp,dest,src)
towerofhanoi(3,'A','C','B')




#josephus problem
#winner of the circular game
def winner(n,k):
    '''circular game leetcode 1823'''
    if n==1:
        return 1
    return (winner(n-1,k)+k-1)%n+1
print(winner(5,2))
