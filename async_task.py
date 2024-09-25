import asyncio

async def async_write_to_file(filename, data, duration):
    """Asynchronously write data to a file with a simulated duration."""
    await asyncio.sleep(duration)  # Simulate some delay in writing
    # Write to file in a non-blocking way
    with open(filename, 'w') as f:
        f.write('\n'.join(map(str, data)))  # Write data to the file
    print(f"Finished writing to {filename}")

async def run_async_tasks():
    """Run multiple file writing tasks asynchronously."""
    # Read the prime numbers from an existing file
    with open('numbers.txt', 'r') as f:
        primes = [int(line.strip()) for line in f.readlines() if line.strip().isdigit()]

    # Prepare the file names and associated data with simulated durations
    tasks = [
        (f'primes_1.txt', primes[:len(primes) // 4], 1),  # 1 second
        (f'primes_2.txt', primes[len(primes) // 4:len(primes) // 2], 2),  # 2 seconds
        (f'primes_3.txt', primes[len(primes) // 2:3 * len(primes) // 4], 1.5),  # 1.5 seconds
        (f'primes_4.txt', primes[3 * len(primes) // 4:], 2.5),  # 2.5 seconds
    ]

    # Create a list of asynchronous tasks
    write_tasks = [async_write_to_file(filename, data, duration) for filename, data, duration in tasks]

    # Run tasks concurrently
    await asyncio.gather(*write_tasks)

