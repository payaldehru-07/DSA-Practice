##Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.Input: n=5, arr = [1,2,3,4,5]

arr = [1,2,3,4,5]
left = 0
right = len(arr)-1
while left<right:
 arr[left] , arr[right] = arr[right] , arr[left]
 left = left+1
 right = right-1
 print(arr)