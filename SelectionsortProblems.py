#implementation
def selectionsort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[64, 25, 12, 22, 11]
print(selectionsort(arr))




#mini and maxi basic logic
def minimaxi(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr[0],arr[-1]
arr=[64, 25, 12, 22, 11]
print(minimaxi(arr))
#3rd max
#179
#215
#sort array using selection sort
