def merge(left,right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

def merge_sort(arr):

    if len(arr)<= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x<pivot]
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]

    return quick_sort(left) + mid + quick_sort(right)

lst = [1,5,3,7,9,2,14]

print(merge_sort(lst))
print(quick_sort(lst))