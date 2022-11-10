#Function for Valid Mountain Array
def valid_mountain_array(arr):
    if len(arr)<3 or  arr[0] == max(arr) or arr[-1] == max(arr):
        return False
    l = 0
    r = len(arr)-1
    while(l<len(arr) and arr[l]<arr[l+1]):
        l += 1
    while(r>0 and arr[r]<arr[r-1]):
        r -= 1
    return l==r

arr = [10,2,5,3]
k = valid_mountain_array(arr)