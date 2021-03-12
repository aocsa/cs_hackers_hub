# %%
# runtime complexity:  
import random
# space complexity:  
    # recursive ver: O(log n) vs O(1)
    # iterative ver: 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] # rand.random
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5, 3, 7, 2, 10]))
# [5, 3, 7, 2, 10]
# rank-1: 2
# rank-2: 3
# rank-3: 5
# ...
# runtime complexity:   O(n)  
# space complexity:  
def partition(arr, pivot, low, high):
    pivot_val = arr[pivot]
    arr[pivot], arr[low] = arr[low], arr[pivot] 
    left = [x for x in arr[low+1:high+1] if x < pivot_val]
    right = [x for x in arr[low+1:high+1] if x >= pivot_val]
    for index, value in enumerate(left):
        arr[low + index] = value
    new_pivot = low + len(left)
    arr[new_pivot] = pivot_val

    for index, value in enumerate(right):
        arr[new_pivot + 1 + index] = value
    return new_pivot

def quick_select_rec(arr, low, high, topk):
    if low == high:
        return arr[low]
    else:
        pivot_idx = random.randrange(low, high+1)
        pivot_idx = partition(arr, pivot_idx, low, high)
        
        if topk == pivot_idx:
            return arr[topk]
        if topk < pivot_idx:
            return quick_select_rec(arr, low, pivot_idx - 1, topk)
        else:    
            return quick_select_rec(arr, pivot_idx + 1, high, topk)

def quick_select(arr, topk):
    return quick_select_rec(arr, 0, len(arr) - 1, topk - 1)

print(quick_select([5, 3, 7, 2, 10], 1))

# %%

# TODOS: 
    # 