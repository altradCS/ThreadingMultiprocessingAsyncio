# multiprocessing_task.py
from multiprocessing import Pool
import math

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def process_chunk(numbers):
    """Process a chunk of numbers to find primes."""
    return [n for n in numbers if is_prime(n)]

def multiprocessing_prime(filename='numbers.txt'):
    """Reads numbers from file and checks for primes using multiprocessing."""
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f]

    # Split the data into chunks (you can adjust the chunk size)
    chunk_size = len(numbers) // 4  # Assuming 4 CPU cores
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    # Use multiprocessing to process each chunk
    with Pool() as pool:
        results = pool.map(process_chunk, chunks)

    # Combine the results from all processes
    primes = [prime for sublist in results for prime in sublist]
    print(f"Found {len(primes)} prime numbers.")
    return primes

if __name__ == '__main__':
    multiprocessing_prime()
