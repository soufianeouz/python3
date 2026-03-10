def ft_prime(n):
    prime_num = 2
    i = 0
    while i < 5:
        j = 2
        check = 1
        while j < prime_num:
            if prime_num%j == 0:
                check = 0
                break
            j+=1
            
        if check == 1:
            i+=1
            yield prime_num
        prime_num+=1

n = 5
count = 0
for i in ft_prime(n):
    if count < n - 1:
        print(i, end=", ")
    else:
        print(i)
    count+=1
# print(next(g))