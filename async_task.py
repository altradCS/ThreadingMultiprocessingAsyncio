import asyncio
import aiofiles

async def async_write_to_file(file_path, data_chunk, wait_time):
    print(f"Writing {file_path}...")
    
    await asyncio.sleep(wait_time)
    async with aiofiles.open(file_path, 'w') as file:
        await file.write('\n'.join(map(str, data_chunk)))
    print(f"Writing complete: {file_path}.")

async def run_async_tasks(prime_numbers):
    output_files = ["prime_numbers_1.txt", "prime_numbers_2.txt", "prime_numbers_3.txt"]
    tasks = []
    total_primes = len(prime_numbers)
    chunk_size = total_primes // len(output_files)
    extra_primes = total_primes % len(output_files)

    index = 0
    for file_index in range(len(output_files)):
        if file_index < extra_primes:
            current_chunk = prime_numbers[index:index + chunk_size + 1]
            index += chunk_size + 1
        else:
            current_chunk = prime_numbers[index:index + chunk_size]
            index += chunk_size

        if current_chunk:
            file_name = output_files[file_index]
            delay = 0.5
            tasks.append(async_write_to_file(file_name, current_chunk, delay))

    await asyncio.gather(*tasks)
    print("All asynchronous write operations successfully executed.")