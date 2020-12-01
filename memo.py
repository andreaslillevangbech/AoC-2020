def memoize(f):
  memo = {}
  def wrapper(x):
    if x not in memo:            
      memo[x] = f(x)
    return memo[x] 
  return wrapper

@memoize
def fib(n):
  if n<2:
    return n
  else:
    return fib(n-1) +  fib(n-2)

print(fib(40))
