primes = []
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True
for num in range(0, 21):
    if is_prime(num):
        primes.append(num)
print(primes)
