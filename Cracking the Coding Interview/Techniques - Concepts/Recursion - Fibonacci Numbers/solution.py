fib = {0: 0, 1: 1}

def fibonacci(n):
    if n in fib:
        return fib[n]
    else:
        fib[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib[n]
    
n = int(input())
print(fibonacci(n))