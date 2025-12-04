#implementation of binary search
def binarysearch(arr,key):
    arr.sort()
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif key<arr[mid]:
            high=mid-1
        else:
            low=mid+1
arr=list(map(int,input("").split()))
key=int(input(""))
print(binarysearch(arr,key))

#implementationof binary serach useing recursion
def binarysearch(arr,low,high,key):
    arr.sort()
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif key<arr[mid]:
            return binarysearch(arr,low,mid-1,key)
        else:
            return binarysearch(arr,mid+1,high,key)
arr=list(map(int,input("").split()))
print(binarysearch(arr,low=0,high=len(arr),key=25))

#search insert position
def searchinseartposition(nums,target):
    low,high=0,len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low #we returned low bc in case of the index is not found the search will return the postion that it can be inserted
nums=[1,3,5,6]
target=2
print(searchinseartposition(nums,target))#output will be 1


#first and last position in sorted array
def firstlastposition(arr,target):
    start=-1
    end=-1
    for i in range(len(arr)):
        if arr[i]==target: #iteration 1-> arr[0] is not equal
                           #iteration 3-> arr[3] found arr[4] found
                           #start is not -1 so start will be 3
                           # at index 4 as start is already updated it will return end=4
            if start==-1:
                start=i
            end=i
    return start,end
arr=[1,2,3,4,4,5,6]
target=4
print(firstlastposition(arr,target))


#find the bed version(leetcode-278)

#find the peak element
def peakelemant(arr):
    peak=max(arr)
    return arr.index(peak)
arr=[32,45,67,89,11]
print(peakelemant(arr))
#another method using binary search
def peakelemant(arr):
    low,high=0,len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]<arr[mid+1]:
            low=mid+1
        else:
            high=mid
    return high
arr=[32,45,67,89,11]
print(peakelemant(arr))


#search in rotated sorted array
def rotatedSortedArray(arr,key):
    if key in arr:
        return arr.index(key)
    else:
        return -1
arr=[4,5,6,7,0,1,2,3]
key=0
print(rotatedSortedArray(arr,key))

#koko eating bananas


#capacity to ship packages with D days




#aggressive cows





#allocate minimum pages




#median in 2 sorted arrays
def median(nums1,num2):
    merged_array=[]
    i=j=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merged_array.append(nums1[i])
            i+=1
        merged_array.append(nums2[j])
        j+=1
    merged_array.extend(nums1[i:])
    merged_array.extend(nums2[j:])
    n=len(merged_array)
    mid=n//2
    if n%2==0:
        return merged_array[mid]
    return (merged_array[mid-1]+merged_array[mid])//2
nums1=[1,2]
nums2=[4]
print(median(nums1,nums2))
  


#square root
import math
def squareroot(num):
    return math.sqrt(num)
num=5
print(squareroot(num))


#seach in infinity sorted array
def searchInInfinitySortedArray(nums,low,high,key):
    low=0
    high=1
    while nums[high]<key:
        low=high
        high*=2
    return searchInInfinitySortedArray(nums,low,high,key)
nums=[1,3,5,8,9]
key=5
print(searchInInfinitySortedArray(nums,low,high,key)) #this is used in interviews where they will manage the limits of the high
