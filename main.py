import multiprocessing_task
import multiprocessing
import threading_task
import async_task
import generate_numbers

def main():
    # Step 1: Generate a file with random numbers
    print("Creating the numbers.txt file...")
    generate_numbers.create_file_with_random_numbers("numbers.txt", 10000, 100000, 1000000)
    
    # Step 2: Read the generated numbers from the file
    with open("ThreadingMultiprocessingAsyncio/numbers.txt", "r") as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    # Step 3: Perform multiprocessing to find prime numbers
    print("\nExecuting multiprocessing task to find prime numbers...")
    primes = multiprocessing_task.find_primes_in_chunks(numbers, chunk_size=len(numbers) // multiprocessing.cpu_count())
    print(f"Identified prime numbers: {primes}")

    # Step 4: Execute threading tasks to simulate I/O operations
    print("\nExecuting threading I/O tasks...")
    threading_task.execute_io_tasks()

    # Step 5: Execute asynchronous tasks
    print("Executing asynchronous I/O tasks...")
    import asyncio
    asyncio.run(async_task.execute_async_tasks(primes))

if __name__ == "__main__":
    main()
