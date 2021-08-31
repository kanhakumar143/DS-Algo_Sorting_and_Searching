def psrtition(a, l, h):
    i = l -1 
    pivot = a[h]
    
    for j in range(l, h):
        if a[j] <= pivot:
            i = i+1
            swap(a,i,j)
            # a[i], a[j] = a[j], a[i]

    # a[i+1], a[h] = a[h], a[i+1]
    swap(a, i+1, h)
    return (i+1)

def quickSort(a, l, h):
    if len(a) == 1:
        return a
    if(l < h):
        pi = psrtition(a, l, h)
        quickSort(a, l, pi-1)
        quickSort(a, pi+1, h)

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

if __name__ == '__main__':
  # Driver code
  a= [13, 4, 9, 5, 3, 16, 12]
  quickSort(a, 0, len(a)-1)
  print("sorted arr is : ")
  for i in range(len(a)):
      print("%d" %a[i])
