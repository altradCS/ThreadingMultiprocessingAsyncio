import multiprocessing_task
import threading_task
import async_task
import generate_numbers
import multiprocessing

def main():
    try:
        # Step 1: Generate numbers file
        print("Generating numbers.txt file...")
        generate_numbers.generate_numbers_file("numbers.txt", 10000, 100000, 1000000)
        
        # Step 2: Read numbers from file
        try:
            with open("numbers.txt", "r") as f:
                numbers = [int(line.strip()) for line in f.readlines()]
        except FileNotFoundError:
            print("Error: numbers.txt file not found.")

        except ValueError:
            print("Error: Invalid number format in numbers.txt.")
           
        
        # Step 3: Run multiprocessing task to find primes
        print("Running multiprocessing task...")
        try:
            chunk_size = max(1, len(numbers) // multiprocessing.cpu_count())
            primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size=chunk_size)
            print(f"Prime numbers found: {primes}")
        except Exception as e:
            print(f"An error occurred during multiprocessing: {e}")

        
        # Step 4: Run threading task to simulate I/O
        print("Running threading I/O tasks...")
        try:
            threading_task.run_io_tasks()
        except Exception as e:
            print(f"An error occurred during threading: {e}")
        
        print("Running async I/O tasks...")

        # Step 5: Run async tasks
        try:
            import asyncio
            asyncio.run(async_task.run_async_tasks(primes))
        except Exception as e:
            print(f"An error occurred during async tasks: {e}")


    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()