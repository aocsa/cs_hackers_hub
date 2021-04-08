import math

# %% find 4 numbers
# a^2 + b^2 + c^2 + d^2 = n

def find_4_numbers(n):
    limit = int(math.sqrt(n))
    list = []
    for a in range(1, limit):
        for b in range(a, limit):
            for c in range(b, limit):
                for d in range(c, limit):
                    if a*a + b*b + c*c + d*d == n:
                        item = [d, c, b, a]
                        res = int("{}{}{}{}".format(d, c, b, a))
                        list.append((res, item))
    
    return max(list, key=lambda item : item[0] )[1]

print(find_4_numbers(16))
print(find_4_numbers(110))
# %%
