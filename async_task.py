import asyncio
import aiofiles

async def write_prime_file(primes, filename):
    """Asynchronously writes prime numbers to a file."""
    print(f"Starting to write {len(primes)} primes to {filename}...")
    async with aiofiles.open(filename, 'w') as f:
        for prime in primes:
            await f.write(f"{prime}\n")
    print(f"Finished writing primes to {filename}.")

async def async_write_primes(primes):
    """Splits primes into multiple files and writes them asynchronously."""
    chunk_size = len(primes) // 3  # Adjust how many primes per file
    chunks = [primes[i:i + chunk_size] for i in range(0, len(primes), chunk_size)]

    tasks = []
    for i, chunk in enumerate(chunks):
        tasks.append(write_prime_file(chunk, f"primes_{i+1}.txt"))

    await asyncio.gather(*tasks)  # Run all tasks concurrently

if __name__ == '__main__':
    import aiofiles
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Placeholder, replace with actual primes
    asyncio.run(async_write_primes(primes))
