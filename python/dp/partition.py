# **Problem Statement 
# 
# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# Input:{1,2,3,4}
# Output:True
# {1,4}&{2,3} => 5 | 5

#Input:{1,1,3,4,7}
#Output:True
#{1,3,4}&{1,7} => 8 | 8

#Input:{2,3,4,6} = sum => 15??
#Output:False

# can_partition_rec([1, 2, 3, 4], target=5)

# f(A = [1, 2, 3, 4], target=5)

# base case 1: f(A=[], x) <- 0
# base case 2: f(A=[...], 0) <- 1

# recursive case:
#   f(A, x) => f(A[1:], x - A[0]) + f(A[1:], x)

def can_partition_rec(A, x):
    if len(A) == 0:
        return False
    if x == 0:
        return True

    f1 = False
    if x >= A[0]:
        f1 = can_partition_rec(A[1:], x - A[0])
    f2 = can_partition_rec(A[1:], x)
    return f1 or f2

def can_partition(elems):
    s = sum(elems)
    if s % 2 != 0:
        return False
    return can_partition_rec(elems, s // 2 )


def can_partition_rec_2(A, x, path):
    if len(A) == 0:
        return False
    if x == 0:
        print(path)
        return True
    f1 = False
    if x >= A[0]:
        f1 = can_partition_rec_2(A[1:], x - A[0], path + [A[0]])
    f2 = can_partition_rec_2(A[1:], x, path)
    return f1 or f2

def can_partition_dp(elems):
    print("problem: ", elems)
    s = sum(elems)
    if s % 2 != 0:
        return False
    return can_partition_rec_2(elems, s // 2, [])

class Partition:
    def __init__(self):
        self.memo = {}
        self.path = {}

    def can_partition_rec_dp(self, A, x, path):
        key = (len(A), x)
        if key in self.memo:
            return self.memo[key]
        if len(A) == 0:
            return False
        if x == 0:
            self.path = path
            return True

        f1 = False
        if x >= A[0]:
            f1 = self.can_partition_rec_dp(A[1:], x - A[0], path + [A[0]])
        f2 = self.can_partition_rec_dp(A[1:], x, path)
        self.memo[key] = f1 or f2
        return f1 or f2

    def run(self, elems):
        self.memo = {}
        self.path = {}
        s = sum(elems)
        if s % 2 != 0:
            return False
        out = self.can_partition_rec_dp(elems, s // 2, [])
        other = elems.copy()
        for o in self.path:
            other.pop(other.index(o))
        print(self.path, other)
        return out

s = Partition()
print(s.run([1, 2, 3, 4])) # True
print(s.run([1, 1, 3, 4, 7])) # True
print(s.run([2, 3, 4, 6])) # False

