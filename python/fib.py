
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# DP

# 1. memoization
memo = {}
# runtime complexity: O(n)
# space complexity: O(n)
def fib_memo(n):
    global memo
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    f = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = f
    return f

# 2. tabulation
# runtime complexity: O(n)
# space complexity: O(n)
def fib_tab(n):
    if n < 2:
        return n
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

for i in range(0, 10):
    print(fib(i), fib_memo(i), fib_tab(i))
