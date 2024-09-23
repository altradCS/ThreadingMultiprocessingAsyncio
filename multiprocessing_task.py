import multiprocessing

def is_prime(n):
  if n <= 1:
      return False
  for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
          return False
  return True

def check_prime_chunk(numbers):
  return [number for number in numbers if is_prime(number)]

def find_primes_in_range(numbers, chunk_size):
  number_chunk = [numbers[i * chunk_size:(i + 1) * chunk_size] for i in range(multiprocessing.cpu_count())]
  
  # Use multiprocessing to check the chunks for prime
  with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
      result = pool.map(check_prime_chunk, number_chunk)
      
  return [prime for chunk in result for prime in chunk]