def bubble_sort(arr):
  size = len(arr)
  for i in range(0, size-1):
    for j in range(0, size-i-1):
      if(arr[j+1] < arr[j]):
        swap(arr, j+1, j)
        
def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

if __name__ == '__main__':
  # Driver code
  arr= [13, 4, 9, 5, 3, 16, 12]
  bubble_sort(arr)
  print(arr)