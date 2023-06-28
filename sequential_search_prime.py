def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sequential_search_prime(data):
    primes = []
    for number in data:
        if is_prime(number):
            primes.append(number)
    return primes

my_list = [7, 10, 13, 6, 17, 22, 19]
prime_numbers = sequential_search_prime(my_list)
print("Bilangan prima dalam daftar adalah:", prime_numbers)
