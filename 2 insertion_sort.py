def insertionSort(a):
    n = len(a)

    for i in range(1, n):
        temp = a[i]
        j = i-1

        while(j >= 0 and a[j] > temp):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp

if __name__ == '__main__':
  # Driver code
  a= [13, 4, 9, 5, 3, 16, 12]
  insertionSort(a)
  print("sorted arr is : ")
  for i in range(len(a)):
      print("%d" %a[i])