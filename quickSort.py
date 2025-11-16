def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low -1

        for j in range(low, high):
            if arr[j] <= pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    
    def quicksort(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort(low, pi-1)
            quicksort(pi+1, high)
        
    quicksort(0, len(arr)-1)
    return arr

nums = [10, 7, 8, 9, 1, 5]
print(quick_sort(nums))
'''
control flow: print -> q_s-> -> quicksort -> [partition -> rec.quicksort] -> return arr.

'''
