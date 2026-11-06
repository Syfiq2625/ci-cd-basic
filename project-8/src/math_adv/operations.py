def add(*args):
    return sum(args)

def multiply(*args):
    if not args:
        return 0
    result = 1
    for num in args:
        result *= num
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
