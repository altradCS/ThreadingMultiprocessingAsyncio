import multiprocessing

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    """Check primality for a chunk of numbers."""
    return [n for n in numbers if is_prime(n)]

def find_primes_in_range(numbers, chunk_size):
    """Split numbers into chunks and use multiprocessing to find primes."""
    with multiprocessing.Pool() as pool:
        chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
        prime_chunks = pool.map(check_prime_chunk, chunks)
    return [prime for chunk in prime_chunks if chunk for prime in chunk]
