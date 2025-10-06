# Fibonacci, Dynamic Programming without Memoization:

counterrr = 0 

def fibbb(n): 
    global counterrr
    counterrr += 1 # track the number of function-calls 
    
    if n == 0 or n == 1:
        return n
    
    return fibbb(n-1) + fibbb(n-2)


n = 35
print('\n Fib of', n, '=', fibbb(n))
print('\n Counter (aka. number of funtion-calls): ', counterrr) 

# Analysis: 
# if n = 7, then counter = 41
# if n = 20, then counter = 21891!
# if n = 30, then counter >= 2 M!
# if n = 35, then counter >= 29 M!
# so, it's very inefficinet! 
# Therefore, DP almost always uses 'Memoization' when using recursion to make the program efficient! 
# complexity = o(n^2)
#################################################################
# same as above, but with Memoization:

counterr = 0 
memo = [None] * 100

def fibb(n): 
    global counterr
    counterr += 1 # track the number of function-calls 
    
    if memo[n] is not None: 
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fibb(n-1) + fibb(n-2)
    return memo[n]



n = 35
print('\n Fib of', n, '=', fibb(n))
print('\n Counter (aka. number of funtion-calls): ', counterr) 

# Analysis: 
# now, if n = 35, then counter = 69! 
# so the code became more efficient! 
# complexity = O(2n-1) = o(n)
# Lesson learned: if we are goona do dynamic programming recursively, we need memoization, or it will be veryyy inefficient. 
#################################################################
# The approach in above was 'top-bottom'. 
# same as above with memoization, but 'bottom-up': 

counter = 0 

def fib(n): 
    global counter
    counter += 1

    fib_list = [0, 1]
    for i in range(2, n+1): 
        # or 'counter += 1' here which would be equal to (n-1)
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib) 

    return fib_list[n]


n = 35
print('\n Fib of', n, '=', fib(n))
print('\n Counter (aka. number of funtion-calls): ', counter) 

# Analysis: 
# only 1 function-call, and then retrieval from the list 
# complexity = o(n-1) = o(n)
# but the downside is even though we get better time complexity result, but we are using more memory. 

