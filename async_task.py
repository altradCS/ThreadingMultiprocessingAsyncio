# Part 3: Async IO with Non-blocking I/O-bound Tasks
#     In this part, you will perform file writing tasks asynchronously using async IO. You will simulate writing results to files asynchronously, which can help you manage a large number of I/O operations without blocking the program.

#     Steps:
#        Use Async IO for writing files:
#         1. Write the prime numbers calculated in Part 1 to multiple files asynchronously.
#         2. Ensure the program doesn’t block while writing to files.


import asyncio

async def async_write_to_file(filename, data, duration):
    # Simulate I/O-bound task by writing to a file
    print(f"Writing {filename}...")
    await asyncio.sleep(duration)
    print(f"{filename} written.")

    # Write data to file
    with open(filename, "w") as f:
        f.write(data)

async def run_async_tasks(primes):
    # Simulate writing results to multiple files asynchronously
    filenames = ["primes1.txt", "primes2.txt", "primes3.txt"]
    # Split numbers into chunks
    chunk_size = len(primes)//len(filenames)
    chunks = [primes[i:i + chunk_size] for i in range(0, len(primes), chunk_size)]

    # Create tasks to write chunks to files
    tasks = []
    for i in range(len(filenames)):
        filename = filenames[i]
        data = "\n".join(map(str, chunks[i]))
        task = asyncio.create_task(async_write_to_file(filename, data, 1))
        tasks.append(task)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    print("Async I/O tasks completed.")






    



    
