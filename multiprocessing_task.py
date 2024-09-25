import multiprocessing
import requests

def is_prime(n):
    
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    return [is_prime(num) for num in numbers]

def find_primes_in_range(numbers, chunk_size):

    with multiprocessing.Pool() as pool:
        chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
        results = pool.map(check_prime_chunk, chunks)
    primes = [prime for sublist in results for prime in sublist]
    return primes