# Part 1: Multiprocessing with CPU-bound Tasks
#   In this part, you will use multiprocessing to process a file containing a list of large numbers and calculate whether each number is prime. This task will involve splitting the data across multiple processes to fully utilize the CPU.

#     Steps:
#     1 Upload the data:
#        Upload a file (numbers.txt) containing a list of large numbers (one per line) to GitHub repository.
#        Download the file in your Python code using a URL.
    
#     2. Process the file using multiprocessing:
#        Create a function that reads the file, divides the data into chunks, and uses the multiprocessing.Pool to calculate whether each number is prime.
#        Use the is_prime function to check if a number is prime.


import multiprocessing

def is_prime(n):
    """Check if a number is prime (CPU-bound task)."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    """Check if numbers in a chunk are prime."""
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes
  

def find_primes_in_range(numbers, chunk_size):
    """Find prime numbers in a list of numbers using multiprocessing."""
    # Split numbers into chunks
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Create a process pool
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the check_prime_chunk function to each chunk
        results = pool.map(check_prime_chunk, chunks)
    
    # Flatten the results
    primes = [prime for prime_list in results for prime in prime_list]
    return primes

