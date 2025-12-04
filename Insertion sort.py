#insertion sort
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        print(f"\nInserting {key} into sorted part {arr[:i]}")
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(f"Result: {arr}")
    return arr
arr=[23,78,90,34,12,2]
print(insertionsort(arr))
