import asyncio

def write_to_file(file_name, datas):
    print(f"Start writing to {file_name}...")
    
    with open(file_name, 'w') as f:
        f.write(datas)
        
    print(f"Finished writing to {file_name}.")
    
    
async def async_write_to_file(file_name, datas, duration):  
    await asyncio.sleep(duration)
    await asyncio.to_thread(write_to_file, file_name, datas)

async def run_async_tasks(datas):
    file_names = ["prime1.txt", "prime2.txt", "prime3.txt", "prime4.txt", "prime5.txt"]
    data_str = ", ".join(map(str, datas))
    
    tasks = [async_write_to_file(file_name, data_str, 1) for file_name in file_names]
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    print("All async file complete")
