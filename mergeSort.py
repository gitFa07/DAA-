def merge_sort(arr):
    # recursive part 
    if len(arr)<=1:
        return arr # base case
    
    mid = len(arr) // 2
    left = merge_sort(arr[ : mid])
    right = merge_sort(arr[mid : ])

    return merge(left, right)

def merge(left, right):
    merged= []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]<= right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    
    # append remaining elements 

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

data = [2, 8, 5, 3, 9, 4, 1, 7]
print(merge_sort(data))

'''
rec partL:
    base case
    
    rec part 
    
    past left, right ls to build

build part:
    append samllest from left most of both ls

    .extend for remaining elements 

    return merged ls

print ls
    '''