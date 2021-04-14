# Coin Change
# You are given coins of different denominations and a total amount of money. Write a function to
# compute the number of combinations that make up that amount. You may assume that you have
# infinite number of each kind of coin.

# Input: amount = 5, coins = [1, 2, 5]

# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Input: amount = 6
# coins = [1, 5]
# 6 = 1 + 1 + 1 + 1 +1 + 1
# 6 = 1 + 5

# f([1, 5], 6)
    # f([1, 5], 5)
        # f([1, 5], 4)
            # f([1, 5], 3)
                # f([1, 5], 2)
                    # f([1, 5], 1)
                        # f([1, 5], 0) <- one solution
        # f([5], 4)
            # the end 
    # f([5], 5)
        # f([5], 0) <- another solution

# Examples: Input: arr[] = {1, 2, 3, 3}, X = 6
# Output: 3 
# All the possible subsets are {1, 2, 3}, {1, 2, 3} and {3, 3}
def F(A, n, x):
    key = (n, x)
    if x == 0:
        return 1
    if n < 0:
        return 0
    else:
        f2 = f1 = 0
        if x >= A[n]: 
            f1 = F(A, n-1, x - A[n])
        f2 = F(A, n-1, x)
        f = f1 + f2
        return f 

# runtime complexity O(2^len(coins))
def f(coins, n, path):
    if len(coins) == 0:
        return 0
    if n == 0: 
        print(path)
        return 1
    count = 0 
    for i in range(len(coins)):
        if n >= coins[i]:
            count += f(coins[i:], n - coins[i], path + [coins[i]])
    return count

    
# A =[1, 2, 3, 3]
# print(F(A, len(A) - 1, 6) ) # 3

# runtime: O(n * len(coins))  
# space: O(n * len(coins))
memo = {}
def f(coins, n, path):
    global memo
    key = (len(coins), n)
    if key in memo:
        c, p = memo[key]
        print(p)
        return c 
    if len(coins) == 0:
        return 0
    if n == 0: 
        print(path)
        return 1
    count = 0 
    for i in range(len(coins)):
        if n >= coins[i]:
            count += f(coins[i:], n - coins[i], path + [coins[i]])
    memo[key] = (count, path)
    return count
    
    
#memo = (len(coins), N)

def ft(coins, N):
    T = [ [0] * (len(coins)) for in range(N + 1)]
    for i in range(len(coins)):
        T[0][i] = 1
    count = 0 
    for i in range(len(coins)):
        for n in range(N+1):
            if n >= coins[i]:
                T[i][n] += T[i][n - coins[i]]
    return T[len(coins)][N]
    
def ft(coins, N):
    t = [0] * (N + 1)
    t[0] = 1

    count = 0 
    for i in range(len(coins)):
        for n in range(N+1):
            if n >= coins[i]:
                t[n] += t[n - coins[i]]
    print(t)
    return t[N]

# print(f(coins=[1, 2, 3, 5], n=32, path = []))
print(ft([1, 2, 3, 5], 32))