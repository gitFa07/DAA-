def heapify(arr, n, i):
    
    largest= i
    left = 2*i + 1
    right = 2*i + 2

    # if left child exisits and larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # if right child exisits and larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if largest is not root swap and continue heapfy 
    if largest!= i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) # rec call heapfy

def buildMaxHeap(arr):
    
    n= len(arr)

    # last left node 
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

def heapSort(arr):
    n = len(arr)

    buildMaxHeap(arr)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0) # heapfy reduced heap 

    return arr

arr= [3, 19, 1, 14, 8, 7]
print(heapSort(arr))