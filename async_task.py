import asyncio
import aiofiles

async def async_write_to_file(filename, data):
    async with aiofiles.open(filename, 'w') as f:
        for number in data:
            await f.write(f"{number}\n")


async def run_async_tasks(number_lists):
    tasks = []
    
    for idx, number_list in enumerate(number_lists):
        filename = f'PrimeIn_chunk_{idx+1}.txt'
        tasks.append(async_write_to_file(filename, number_list))
        print("Completed writing to file: ", filename)

    # Run all write tasks concurrently
    await asyncio.gather(*tasks)
