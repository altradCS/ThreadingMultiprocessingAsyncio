import asyncio

async def async_write_to_file(filename, data):
    print(f"Writing to {filename}...")
    await asyncio.sleep(1)  # Simulating I/O operation
    with open(filename, "w") as f:
        f.write("\n".join(map(str, data)))
    print(f"Finished writing to {filename}")

async def run_async_tasks(prime_chunks):
    tasks = []
    for i, primes in enumerate(prime_chunks):
        tasks.append(async_write_to_file(f"primes_{i}.txt", primes))
    
    await asyncio.gather(*tasks)

