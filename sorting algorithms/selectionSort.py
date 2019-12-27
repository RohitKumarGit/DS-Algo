"""
selction sort

- we keep
"""
def swap(arr,i1,i2):
    temp=arr[i1]
    arr[i1]=arr[i2]
    arr[i2]=temp
def selctionSort(arr):
    for count in range(len(arr)):
        head=arr[count]
        min = head
        for number in arr[count:]:
            if number < min :
                min = number
                minIdx=arr.index(number)
        swap(arr,count,minIdx)
    return arr
