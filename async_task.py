import asyncio
import aiofiles

async def write_data_to_file(file_name, data, delay):
    print(f'Starting to write data to {file_name}')
    await asyncio.sleep(delay)
    async with aiofiles.open(f'ThreadingMultiprocessingAsyncio/{file_name}', 'w') as file:
        for number in data:
            await file.write(f'{number}\n')
    print(f'Finished writing to {file_name}')

async def execute_async_tasks(prime_numbers):
    total_files = 5
    tasks = []
    chunk_size = len(prime_numbers) // total_files
    for i in range(total_files):
        file_name = f'prime{i+1}.txt'
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < total_files - 1 else len(prime_numbers)  # For the last file, use the length of the prime list
        data_chunk = prime_numbers[start:end]
        delay = 0.5
        
        task = asyncio.create_task(write_data_to_file(file_name, data_chunk, delay))
        tasks.append(task)
        
    await asyncio.gather(*tasks)
    print("All writing tasks have been completed.")
