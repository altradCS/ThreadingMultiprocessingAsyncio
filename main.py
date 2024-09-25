import multiprocessing_task
import multiprocessing
import threading_task
import async_task

def main():
    #get file from github
    threading_task.run_io_tasks(files=["https://raw.githubusercontent.com/S0KPiseth/Class/refs/heads/main/numbers.txt",])
    try:
        with open("numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        print("File not found.")
        return


    # Step 3: Run multiprocessing task to find primes

    ## Note: this will check numbers concurrently
    print("Running multiprocessing task...")

    primes_in_chunks = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
    primes = [prime for chunk_primes in primes_in_chunks for prime in chunk_primes]
    print(f"Prime numbers found: {primes}")

    # Step 4: Run threading task to simulate I/O
    # Note: this will download files multiple files concurrently
    files = [
        "https://raw.githubusercontent.com/S0KPiseth/4k-youtube-downloader-with-UI/refs/heads/main/functions.py",
        "https://raw.githubusercontent.com/S0KPiseth/MultiTimer/refs/heads/main/UI.py",
    ]
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks(files=files)

    # Step 5: Run async tasks
    # Note: this will write prime numbers obtain from multiprocessing and write the answer to files concurrently
    print("Running async I/O tasks...")
    import asyncio
    asyncio.run(async_task.run_async_tasks(primes_in_chunks))

if __name__ == "__main__":
    main()
