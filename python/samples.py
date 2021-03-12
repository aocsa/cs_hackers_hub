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

def f(n):
  val=0
  for i in range(n): # O(n)
    for j in range(i): #-, 0, 1, 12, 123, 1234, ... 
      val+=1
      print('@', end='')
    print()

f(10)

# %%
# binary_search(n)
def binary_search_rec(arr, key, begin, end):
  mid = (begin + (end - begin) // 2)
  if key == arr[mid]:
    return True
  if begin == end:
    return False
  if key < arr[mid]:
    return binary_search_rec(arr, key, begin, mid - 1)
  else: 
    return binary_search_rec(arr, key, mid + 1, end)
  
def binary_search(arr, key):
  return binary_search_rec(arr, key, 0, len(arr) - 1)
  
arr = [1, 3, 5, 7, 9] #=> log(5) = 
print(binary_search(arr, key=3))
print(binary_search(arr, key=4))
# %%


# %%
# def fib(n):
#   if n < 2:
#     return n
#   return fib(n-1) + fib(n-2)

def fib(n):
  if n < 2:
    return n
  f = [0] * (n+1)
  f[0] = 0
  f[1] = 1
  for i in range(2, n+1): # O(n)
    f[i] = f[i-1] + f[i-2] 
  return f[n]
for i in range(10):
  print(fib(i))

# def fib(n):
#   a = 0
#   b = 1
#   for i in range(2, n): # O(n)
#     tmp = b
#     a = a + b 
#   return f[n]