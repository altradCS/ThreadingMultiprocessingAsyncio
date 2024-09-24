import asyncio

async def async_write_to_file(filename, data):
    """Asynchronously write data to a file."""
    await asyncio.sleep(0)  # Simulating a non-blocking I/O operation
    with open(filename, 'a') as f:
        f.write(data + '\n')

async def run_async_tasks(prime_numbers):
    """Run asynchronous tasks to write prime numbers to multiple files."""
    tasks = []
    for i, prime in enumerate(prime_numbers):
        filename = f'prime_numbers_{i // 100}.txt'  # Create a new file for every 100 primes
        task = async_write_to_file(filename, str(prime))
        tasks.append(task)

    await asyncio.gather(*tasks)

# No example usage in this file; it's called from main.py.
