import asyncio

async def async_write_to_file(filename, data, duration):
    await asyncio.sleep(duration)  # Simulate a time delay for I/O
    with open(filename, "a") as f:
        f.write(data + "\n")
    print(f"Written '{data}' to {filename}.")

async def run_async_tasks():
    tasks = [
        async_write_to_file("async_file.txt", "Data 1", 1),
        async_write_to_file("async_file.txt", "Data 2", 2),
        async_write_to_file("async_file.txt", "Data 3", 3),
    ]
    for i in range(1, 4):
        tasks.append(async_write_to_file("async_file.txt", f"Data {i}", i))
    await asyncio.gather(*tasks)
