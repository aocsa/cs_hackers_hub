
# Dynamic Programming

# Count of subsets with sum equal to X
# Given an array arr[] of length N and an integer X,
# the task is to find the number of subsets with sum equal to X.

# Examples: Input: arr[] = {1, 2, 3, 3}, X = 6
# Output: 3
# All the possible subsets are {1, 2, 3}, {1, 2, 3} and {3, 3}


# runtime : O(2^n)
# space : O(n)
def f(A, x, i, path):
    if x == 0:
        print(path)
        return 1
    if i < 0:
        return 0
    if x >= A[i]:
        f1 = f(A, x - A[i], i - 1, path + [A[i]])
    f2 = f(A, x, i - 1, path)
    return f1 + f2

memo = {}
# runtime : O(n*X)
# space : O(n*X) + O(n) = O(n*X)
def f_m(A, x, i):
    global memo
    key = (x, i)
    if key in memo:
        return memo[key]
    if x == 0:
        return 1
    if i < 0:
        return 0
    if x >= A[i]:
        f1 = f_m(A, x - A[i], i - 1)
    f2 = f_m(A, x, i - 1)
    memo[key] = f1 + f2
    return f1 + f2

# runtime : O(n*X)
# space : O(n*X)
def f_t(A, X):
    n = len(A)
    T = [ [0] * (X+1) for i in range(n+1)]
    # base case
    # f(A, 0, i): = 1
    for i in range(0, n + 1):
        T[i][0] = 1

    for i in range(1, n+1):
        for x in range(1, X + 1):
            f1 = 0
            if x >= A[i-1]:
                f1 = T[i-1][x - A[i-1]]
            f2 = T[i-1][x]
            T[i][x] = f1 + f2
    return T[n][X]

arr = [1, 2, 3, 3]
X = 6
print(f(arr, X, len(arr) - 1, []))
print(f_m(arr, X, len(arr) - 1))
print(f_t(arr, X))






















































