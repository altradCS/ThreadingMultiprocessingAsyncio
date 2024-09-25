import multiprocessing

def is_prime(n):
    """check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_chunk(chunk):
    """check a chunk of numbers and return a list of prime numbers"""
    prime_numbers = [n for n in chunk if is_prime(n)]
    return prime_numbers

def find_primes_in_range(numbers, chunk_size):
  chunks = [numbers[i:i + chunk_size] for i in range (0, len(numbers), chunk_size)] # split dataset into chunks 
  
  with multiprocessing.Pool() as pool:
    results = pool.map(check_chunk, chunks)
  
  return [prime for result in results for prime in result]