import multiprocessing_task
import threading_task
import async_task
import generate_numbers
import multiprocessing
import asyncio

def main():
    # Step 1: Generate numbers file
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers_file("numbers.txt", 10000, 100000, 1000000)
    
    # Step 2: Read numbers from file
    try:
        with open("numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f.readlines()]
            
    except FileNotFoundError:
        print("Error: File 'numbers.txt' not found.")
        return
    
    # Step 3: Run multiprocessing task to find primes
    print("Running multiprocessing task...")
    primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
    print(f"Prime numbers found: {primes}")
    print("Multiprocessing task completed.\n")

    # Step 4: Run threading task to simulate I/O
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks()
    print("Threading I/O tasks completed.\n")

    # Step 5: Run async tasks
    print("Running async I/O tasks...")
    asyncio.run(async_task.run_async_tasks(primes))
    print("Async I/O tasks completed.\n")
    

if __name__ == "__main__":
    main()
