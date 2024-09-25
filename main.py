import multiprocessing_task
import threading_task
import async_task
import generate_numbers
import multiprocessing

def main():
    # step 1: generate numbers file
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers_file("numbers.txt", 10000, 100000, 1000000)
    
    # step 2: open numbers from file
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    # Step 3: run multiprocessing task to get all the prime numbers
    print("Running multiprocessing task...")
    primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
    print(f"Prime numbers found: {primes}")
   

    # Step 4: Run threading task to simulate I/O
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks()
   

    # Step 5: Run async tasks
    print("Running async I/O tasks...")
    import asyncio
    asyncio.run(async_task.run_async_tasks(primes))

if __name__ == "__main__":
    main()
