import multiprocessing

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def check_prime_chunk(numbers):
  return [n for n in numbers if is_prime(n)]

def find_primes_in_range(numbers, chunk_size):
  chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
  with multiprocessing.Pool() as pool:
    result = pool.map(check_prime_chunk, chunks)
  
  primes = [num for sublist in result for num in sublist]
  return primes

# print(is_prime(9))