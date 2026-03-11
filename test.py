def ft_Fibonacci(n):
    f0 = 0
    f1 = 1
    
    i = 0
    while i < n:
        yield f0
        tmp = f0
        f0 = f1
        f1 = f1 + tmp
        i+=1
g = ft_Fibonacci(10)
