import multiprocessing
import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_primes(chunk):
    """Filter prime numbers from a given chunk of numbers."""
    return [num for num in chunk if is_prime(num)]

def find_primes_in_chunks(numbers, chunk_size):
    """Find prime numbers in a list using multiprocessing with chunks."""
    # Divide the list of numbers into smaller chunks based on the chunk size
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Use multiprocessing to check each chunk for prime numbers
    with multiprocessing.Pool() as pool:
        prime_chunks = pool.map(filter_primes, chunks)
    
    # Flatten the list of prime chunks into a single list of prime numbers
    return [prime for primes in prime_chunks for prime in primes]
