def selection_sort(arr):
  n = len(arr)

  # for i in range(n-1):
  #   min_index = i
  #   for j in range(min_index + 1, n):
  #     if arr[j] < arr[min_index]:
  #       min_index = j
  #   if i != min_index:
  #     arr[i], arr[min_index] = arr[min_index], arr[i]


  for i in range(0, n-1):
    min = i
    for j in range(i+1, n):
      if arr[j] < arr[min]:
        min = j

    if min != i:
      swap(arr, min, i)

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
  # Driver code
  arr= [13, 4, 9, 5, 3, 16, 12]
  selection_sort(arr)
  print(arr)

  # a = []
 
  # for i in range(0, 5):
  #    ele = int(input())
  #    a.append(ele)

  # selection_sort(a)
  # print(a)
