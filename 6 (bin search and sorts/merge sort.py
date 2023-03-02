def merge(arr1:list,arr2:list)->list:
    for i in arr2:
        arr1.append(i)
    return arr1

def merge_sort(arr : list,left:int,right:int)-> list:
    if left<right:
        mid=(left+right)//2
        return merge(merge_sort(arr,left,mid),merge_sort(arr,mid+1,right))
    return arr

arr=[int(i) for i in input().split()]
print(merge_sort(arr,0,len(arr)-1))