#valid palindrome
def validpalindrome(s):
    cleaned_sentence=''
    for words in s:
        if words.isalnum():
            cleaned_sentence+=words.lower()
    return cleaned_sentence==cleaned_sentence[::-1]
s='all of us'
print(validpalindrome(s))


#remove duplicates in sorted array
def duplicate(nums):
    nums.sort()
    return set(nums)
nums=[1,2,3,4,5,5]
print(duplicate(nums))





#move zeros to end
def movezeros(arr):
    zero_count=0
    res=[]
    for i in arr:
        if i!=0:
            res.append(i)
        else:
            zero_count+=1
    res.extend([0]*zero_count)
    return res
arr=[1,2,0,3,0,4]
print(movezeros(arr))
            
    
#trapping trapping water
def trappingrainwater(height):
    left=right=[0]*len(height)
    trapped_water=0
    left[0]=height[0]
    right[-1]=height[-1]
    for i in range(1,len(height)):
        left[i]=max(left[i-1],height[i])
    for i in range(len(height)-2,-1,-1):
        right[i]=max(right[i+1],height[i])
    for i in range(len(height)):
        trapped_water+=min(left[i],right[i])-height[i]
    return trapped_water
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingrainwater(height))
#replace element

#3sum closeset
#fruit into baskets
#minimum window substring

