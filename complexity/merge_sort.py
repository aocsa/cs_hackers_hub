# %%

# runtime complexity: O(n)
# space complexity: O(n)
def merge(left, right):
    # left = [1, 3]
    # right = [2, 5, 7]
    # result = [1, 2, 3,  ]
    result = []
    i = 0
    j = 0
    n = len(left) + len(right)
    while len(result) < n:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left):
            result += right[j:]
        if j == len(right):
            result += left[i:]
    return result

# runtime complexity: O(n * log n)
# space complexity: O(log n) + O(n) = O(n)
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

print(merge_sort([5, 3, 7, 2, 10]))
# %%
