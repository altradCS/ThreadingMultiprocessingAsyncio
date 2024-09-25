import multiprocessing

import multiprocessing_task

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    return [n for n in numbers if is_prime(n)]

def find_primes_in_range(numbers, chunk_size):
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    with multiprocessing.Pool() as pool:
        results = pool.map(check_prime_chunk, chunks)
    primes = [prime for sublist in results for prime in sublist]
    return primes
