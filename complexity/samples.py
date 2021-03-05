# %%
def example(n): # O(n^2)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum = sum + 1 # O(1)
            # LOAD SUM R1
            # LOAD 1 R2
            # ADD R1 R2 R3
            # SAVE R3 SUM
    #for i in range(n):
    #	sum *= i
    return sum

for i in range(20):
    print(example(i))

# %%
def sample6(n):
    sum = 0
    pie = 3.14
    j = 1
    for var in range(n):
      if j < var:     
          sum+=1
          j*=2
      else:
        sum+=1
    return sum

for n in [1, 2, 4, 8, 16, 32]:
    print(n, " => ", sample6(n))


# %%
def sample3(n):
    sum = 0
    pie = 3.14
    var = 1
    while var < n:
      for j in range(var):
        sum+=1
      var*=2  
    return sum

for n in [1, 2, 4, 8, 16, 32]:
    print(n, " => ", sample3(n))

#  %% 

def sample(n):
    sum = 0
    pie = 3.14
    var = 1
    while var < n: # 16:  1, 2, 4, 8, 16: log_2(n)
      for j in range(var):
        sum+=1
      var *= 2  
    return sum

print(sample(10))
# %%
