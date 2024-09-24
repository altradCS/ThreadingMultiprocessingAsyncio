import asyncio
import aiofiles

async def async_write_to_file(filename, data, duration):
    print(f'Writing data to {filename}')
    await asyncio.sleep(duration)
    async with aiofiles.open(f'ThreadingMultiprocessingAsyncio\{filename}', 'w') as f:
        for number in data:
            await f.write(f'{number}\n')
    print(f'Done writing to {filename}')

async def run_async_tasks(primes):
    num_files = 5
    tasks = []
    chunk_size = len(primes) // num_files
    for i in range (num_files):
        filename =  f'prime{i+1}.txt'
        start_index = i * chunk_size
        end_index = (i+1) * chunk_size if i < num_files - 1 else len(primes) # if it reaches the last file the end index would simply just the len of the primes list
        data_chunk = primes[start_index:end_index]
        duration = 0.5
        
        task = asyncio.create_task(async_write_to_file(filename, data_chunk, duration))
        tasks.append(task)
        
    await asyncio.gather(*tasks)
    print("All writing tasks completed.")
