#for array in increasing order : awesome workk
# divide and conquer
def binarySearch(tofind,arr):
    if len(arr) == 0 :
        return False
    middle = arr[len(arr)//2]
    

    if middle == tofind :
        return True
    if tofind > middle :
        considerayion=arr[(len(arr)//2) + 1:]
        
    if tofind < middle:
        considerayion = arr[:len(arr)//2]
    result = binarySearch(tofind,considerayion)
    
    return result

print(binarySearch(11,[2,5,8,10]))
