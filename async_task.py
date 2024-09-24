import asyncio
import aiofiles

async def async_write_to_file(filename, data, duration):
    print(f"Starting async write to {filename}")
    
    await asyncio.sleep(duration) 
    async with aiofiles.open(filename, 'w') as file:
        await file.write('\n'.join(map(str, data))) 

    print(f"Finished async write to {filename}")

async def run_async_tasks(primes):
    
    filenames = ["prime1.txt", "prime2.txt", "prime3.txt"]
    tasks = [] 
    num_files = len(filenames)
    total_primes = len(primes)
    
    chunk_size = total_primes // num_files
    remainder = total_primes % num_files

    start_index = 0
    for i in range(num_files):
        if i < remainder:
            chunk = primes[start_index:start_index + chunk_size + 1]
            start_index += chunk_size + 1
        else:
            chunk = primes[start_index:start_index + chunk_size]
            start_index += chunk_size

        if chunk:
            filename = filenames[i]
            duration = 0.5
            tasks.append(async_write_to_file(filename, chunk, duration))

    await asyncio.gather(*tasks)
    
    print("All async file writes completed.")
