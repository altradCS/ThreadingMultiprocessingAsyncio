import multiprocessing
import math

def is_prime(n):
  if n <=1 :
    return False
  if n <= 3 :
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  
  for i in range (5, int(n**0.5)+1, 6):
    if n % i == 0 or n % (i+2) == 0:
      return False
    return True

def check_prime_chunk(chunks):
  return [number for number in chunks if is_prime(number)] # filtering only prime number and put it inside the a list

def find_primes_in_range(numbers, chunk_size):
  chunks = [numbers[i:i + chunk_size] for i in range (0, len(numbers), chunk_size)] # split dataset into chunks 
  
  with multiprocessing.Pool() as pool:
    results = pool.map(check_prime_chunk, chunks)
  
  return [prime for result in results for prime in result] # combine it into one list