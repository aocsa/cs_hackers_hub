#**Problem Statement**

# Given a set of *positive numbers*, partition the set into two subsets with **minimum** difference between their subset sums.
# Return also the two subsets.

### **Example 1:**
#Input:
# A = {1, 2, 3, 9} #
    # {2, 9} vs {1, 3}

# A = {1}
    # A = {1, 2}
        # A = {1, 2}
    # A = {1}
# A = {}
    # A = {2}
    # A = {}

#Output: 3
# {1,2,3} & {9}.


## Example 2:
# Input:{1,2,7,1,5}
# Output:0
# {1,2,5} & {7,1}.
# {1,1,2,5,7}

## example 3:
#Input:{1, 3, 100, 4}
#Output:92
#{1,3,4} & {100}.

from functools import cache

@cache
def can_partition_rec(A, sum1, sum2):
    if len(A) == 0:
        return abs(sum1 - sum2)
    f1 = can_partition_rec(A[1:], sum1 + A[0], sum2)
    f2 = can_partition_rec(A[1:], sum1, sum2 + A[0])
    return min(f1, f2)

def can_partition(A):
    return can_partition_rec(A, sum1=0, sum2=0)

print(can_partition([1, 2, 3, 9])) #3
print(can_partition([1,2,7,1,5])) # 0
print(can_partition([1, 3, 100, 4])) # 92