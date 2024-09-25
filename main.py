import multiprocessing_task
import multiprocessing
import threading_task
import async_task

def main():
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]


    # Step 3: Run multiprocessing task to find primes

    ## Note: this will check numbers concurrently
    print("Running multiprocessing task...")

    primes_in_chunks = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
    primes = [prime for chunk_primes in primes_in_chunks for prime in chunk_primes]
    print(f"Prime numbers found: {primes}")

    # Step 4: Run threading task to simulate I/O
    # Note: this will download files multiple files concurrently
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks()

    # Step 5: Run async tasks
    # Note: this will write prime numbers obtain from multiprocessing and write the answer to files concurrently
    print("Running async I/O tasks...")
    import asyncio
    asyncio.run(async_task.run_async_tasks(primes_in_chunks))

if __name__ == "__main__":
    main()
