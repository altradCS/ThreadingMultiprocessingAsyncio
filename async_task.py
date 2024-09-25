import asyncio
import aiofiles

async def async_write_to_file(filename, data, duration):

    print(f"Starting async write to {filename}")
    
    await asyncio.sleep(duration) 
    async with aiofiles.open(filename, 'w') as file:
        await file.write('\n'.join(map(str, data))) 
    print(f"Finished async write to {filename}")
    
async def run_async_tasks(primes):
    num_files = 5
    tasks = []
    chunk_size = len(primes) // num_files
    for i in range (num_files):
        filename =  f'prime_{i+1}.txt'
        start_index = i * chunk_size
        end_index = (i+1) * chunk_size if i < num_files - 1 else len(primes) 
        data_chunk = primes[start_index:end_index]
        duration = 0.5
        
        task = asyncio.create_task(async_write_to_file(filename, data_chunk, duration))
        tasks.append(task)
        
    await asyncio.gather(*tasks)
    print("All writing tasks completed.")

