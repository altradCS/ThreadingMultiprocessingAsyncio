import multiprocessing

def is_prime(num):
  if num <= 1:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True

def check_prime_chunk(nums):
  return [num for num in nums if is_prime(num)]

def find_primes_in_range(nums, chunk_size):
  num_chunk = [nums[i * chunk_size:(i + 1) * chunk_size] for i in range(multiprocessing.cpu_count())]
  
  #check each chunk for prime numbers
  with multiprocessing.Pool(processes = multiprocessing.cpu_count()) as pool:
      result = pool.map(check_prime_chunk, num_chunk)
      
  return [prime for chunk in result for prime in chunk]
