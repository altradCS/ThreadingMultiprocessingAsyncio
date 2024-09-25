import multiprocessing
from math import isqrt
import urllib.request

import urllib.request

def download_and_read_file(url):
    try:
        response = urllib.request.urlopen(url)
        # Read the content of the file
        data = response.read().decode('utf-8').splitlines()
        
        
        # Convert lines to integers (assuming each line contains one number)
        numbers = [int(line.strip()) for line in data if line.strip().isdigit()]

        
        return numbers

    except urllib.error.URLError as e:
        print(f"Failed to retrieve the file: {e}")
        return []  # Return an empty list if there's an error
    except ValueError as e:
        print(f"Error processing numbers: {e}")
        return []  # Return an empty list if there's a conversion error


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Function to check if numbers in a chunk are prime
def check_prime_chunk(numbers):
    return [n for n in numbers if is_prime(n)]

# Function to find primes using multiprocessing
def find_primes_in_range(numbers, chunk_size):
    # Split the numbers into chunks
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Create a multiprocessing pool
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the check_prime_chunk function to each chunk of numbers
        results = pool.map(check_prime_chunk, chunks)
    
    #  list of results
    primes = [item for sublist in results for item in sublist]
    return primes
