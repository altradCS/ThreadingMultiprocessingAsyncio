import asyncio

# Function to write data to a file (blocking I/O)
def write_to_file(filename, data):
    print(f"Starting to write to {filename}...")
    
    with open(filename, 'w') as f:
        f.write(data)
        
    print(f"Finished writing to {filename}.")
    
    
async def async_write_to_file(filename, data, duration):  
    await asyncio.sleep(duration)
    #  offloads the blocking file I/O operation to a thread
    await asyncio.to_thread(write_to_file, filename, data)


async def run_async_tasks(data):
    filenames = ["prime1.txt", "prime2.txt", "prime3.txt", "prime4.txt", "prime5.txt"]
    data_str = ", ".join(map(str, data))
    
    tasks = [async_write_to_file(filename, data_str, 1) for filename in filenames]
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
