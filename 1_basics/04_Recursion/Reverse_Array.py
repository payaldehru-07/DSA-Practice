##Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

def reverse(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1, right - 1)
arr =[1,2,3,4,5]
reverse(arr, 0, len(arr) - 1)
print(arr)

