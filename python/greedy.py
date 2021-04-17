

# coins = [1, 5, 10, 20, 100]

def coin_change(coins, amount):
    count = 0
    coins = sorted(coins, reverse=True)
    for c in coins:
        while amount >= c:
            amount = amount - c
            count += 1
    return count

# print(coin_change([1, 5, 10, 20, 100], 59))

def knapsack(w, p, M):
    ratio = [pi/wi for pi, wi in zip(p, w)]
    # print(ratio)
    index = list(range(len(w)))
    index.sort(key = lambda i : ratio[i], reverse=True)
    # print(index)
    max_profit = 0
    fractions = [0] * len(w)
    for i in index:
        if M >= w[i]:
            fractions[i] += 1
            max_profit += p[i]
            M = M - w[i]
        else:
            fractions[i] = M / w[i]
            max_profit += fractions[i] * p[i]
            break

    print(fractions)
    return max_profit

print(knapsack(w=[18, 15, 10], p=[25, 24, 15], M=20))
